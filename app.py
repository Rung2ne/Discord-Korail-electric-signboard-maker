import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import re

# .env 파일에서 환경 변수 로드
load_dotenv()

# TOKEN 설정
TOKEN_4 = os.getenv('DISCORD_TOKEN_4')

# 봇 로딩
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            synced = await self.tree.sync()
            print(f'Synced {len(synced)} commands to guild')

        except Exception as e:
            print(f'Error syncing commands: {e}')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

# 색상 태그 정의
COLORS = {
    "<r>": (255, 0, 0),    # 빨강, red
    "<g>": (0, 255, 0),    # 초록, green
    "<y>": (255, 255, 0),  # 노랑, yellow
    "<o>": (255, 165, 0),  # 주황, orange
}

# HTML 스타일 태그를 제거하고 색상을 분리하는 함수
def parse_text_with_colors(text):
    pattern = r"(<[a-z]>|<[a-z]/>|\\n|[^<]+)"
    segments = re.findall(pattern, text)
    parsed = []

    current_color = (255, 255, 255)  # 기본 색상: 흰색
    # 위에 컬러 태그에 없는 색을 치면 흰색으로 출력된다. (<a> 등)

    for segment in segments:
        if segment.startswith("<") and segment.endswith(">"):  # 색상 태그 처리
            current_color = COLORS.get(segment, current_color)
        elif segment == "\\n":  # 줄바꿈 처리
            parsed.append(("\n", current_color))
        else:  # 텍스트 처리
            parsed.append((segment, current_color))
        # HTML 태그와 파이썬의 혼종(?)
        # 사실 띄어쓰기는 %20으로 하려고 했...
    return parsed

# 이미지 생성 함수
def create_board_image(parsed_text):
    # 이미지 크기와 최대 글자 수 설정
    max_width, max_height = 15, 4  # 최대 글자 수 (1줄에 15자, 4줄)
    scale_factor = 200  # 글자 크기 (픽셀 단위)
    image_width, image_height = max_width * scale_factor, max_height * scale_factor
    # 글자 크기를 키우려면 max_width와 max_height를 줄이고, scale_factor은 키워야해요.

    # 검은색 배경의 이미지 생성
    image = Image.new("RGB", (image_width, image_height), "black")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("DungGeunMo.ttf", scale_factor - 20)  # 글자 폰트, 크기 조정

    # 줄바꿈을 기준으로 텍스트 나누기
    lines = []
    current_line = []

    for text, color in parsed_text:
        if text == "\n":  # 줄바꿈 명령어
            if current_line:
                lines.append(current_line)
            current_line = []
        else:
            current_line.append((text, color))

    if current_line:  # 마지막 줄 추가
        lines.append(current_line)

    # 텍스트는 이미지의 중간에 배치
    # 중간이 어디인지 글자 길이에 따라 계산해서 거기에 텍스트 생성
    # 여기는 건드릴게 없어요
    y = (image_height - (len(lines) * (scale_factor - 10))) // 2  # 전체 텍스트를 중앙에 배치

    for line in lines:
        # 줄 전체의 텍스트 조합과 너비 계산
        line_text = "".join([text for text, _ in line])
        line_width = draw.textlength(line_text, font=font)
        x = (image_width - line_width) // 2  # 중앙 정렬 계산

        # 줄의 텍스트를 순차적으로 출력
        offset_x = x
        for text, color in line:
            draw.text((offset_x, y), text, font=font, fill=color)
            offset_x += draw.textlength(text, font=font)  # 텍스트 너비만큼 x 이동

        y += scale_factor - 10  # 다음 줄로 이동

    return image



# 디스코드 명령어 처리
@client.tree.command(name="만들기", description="전광판 이미지를 생성합니다.")
async def 만들기(interaction: discord.Interaction, message: str):
    try:
        # 보낸 메시지에서 텍스트 파싱
        parsed_text = parse_text_with_colors(message)

        # 보낸 메시지의 텍스트와 색상을 반영해 이미지 생성
        board_image = create_board_image(parsed_text)
        board_image.save("board.png")
        # 생성된 이미지는 board.png라 저장됨.

        # 위에서 저장한 board.png 전송
        with open("board.png", "rb") as f:
            # Interaction으로 파일 응답
            await interaction.response.send_message(file=discord.File(f, "board.png"))

    except Exception as e:
        # Interaction 응답에 오류 메시지 전달
        await interaction.response.send_message(f"오류 발생: {e}", ephemeral=True)

client.run(TOKEN_4)
