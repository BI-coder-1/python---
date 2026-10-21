from src.audio_loader import load_wav
file_path = "G:/ICASSP/data/ShipsEar/ShipsEar/shipsear_5s_16k/0/0_0/0_0_1.wav"
print("=== 测试读取正常文件 ===")
try:
    audio = load_wav(file_path)
    print(audio)
except Exception as e:
    print(f"读取失败: {e}")
print("\n=== 测试不存在的文件 ===")
try:
    load_wav("G:/ICASSP/data/not_exist.wav")
except FileNotFoundError as e:
    print(f"成功捕获异常: {e}")
print("\n=== 测试错误格式 ===")
try:
    load_wav("G:/ICASSP/data/test.mp3")
except ValueError as e:
    print(f"成功捕获异常: {e}")

print("\n=== 测试结束 ===")
