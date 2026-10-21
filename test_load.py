from pathlib import Path
from src.audio_loader import load_wav
current_dir = Path(__file__).parent
file_path = current_dir / "samples" / "0_0_1.wav"
non_wav_path = current_dir / "README.md"
print("=== 测试读取正常文件 ===")
try:
    audio = load_wav(str(file_path))
    print(audio)
except Exception as e:
    print(f"读取失败: {e}")
print("\n=== 测试不存在的文件 ===")
try:
    load_wav(str(current_dir / "samples" / "not_exist.wav"))
except FileNotFoundError as e:
    print(f"成功捕获异常: {e}")
print("\n=== 测试错误格式 ===")
try:
    load_wav(str(non_wav_path))
except ValueError as e:
    print(f"成功捕获异常: {e}")

print("\n=== 测试结束 ===")
