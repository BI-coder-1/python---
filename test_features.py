import numpy as np
from pathlib import Path
from src.audio_loader import load_wav
from src.audio_features import extract_features

current_dir = Path(__file__).parent
sample1 = current_dir / "samples" / "0_0_1.wav"
sample2 = current_dir / "samples" / "4_0_1.wav"

print("=== 测试 1：人工构造数组验证 ===")
class DummyAudio:
    data = np.array([0.0, -1.0, 1.0, 0.5])

manual_feat = extract_features(DummyAudio())
print(f"  峰值幅度: {manual_feat['peak_amplitude']} ")
print(f"  平均值: {manual_feat['mean']} ")
print(f"  平均绝对幅度: {manual_feat['mean_absolute_amplitude']} ")
print(f"  总能量: {manual_feat['total_energy']} ")
print(f"  平均能量: {manual_feat['average_energy']} ")
print(f"  RMS: {manual_feat['rms']} ")

is_close = np.isclose(manual_feat['rms']**2, manual_feat['average_energy'])
print(f"  验证 RMS² ≈ 平均能量: {is_close}")

print("\n=== 测试 2：真实样本 0_0_1.wav ===")
try:
    audio1 = load_wav(str(sample1))
    feat1 = extract_features(audio1)
    for k, v in feat1.items():
        print(f"  {k}: {v:.6f}")
except Exception as e:
    print(f"读取失败: {e}")

print("\n=== 测试 3：真实样本 4_0_1.wav ===")
try:
    audio2 = load_wav(str(sample2))
    feat2 = extract_features(audio2)
    for k, v in feat2.items():
        print(f"  {k}: {v:.6f}")
except Exception as e:
    print(f"读取失败: {e}")

print("\n=== 测试 4：空数组异常捕获 ===")
class EmptyAudio:
    data = np.array([])
try:
    extract_features(EmptyAudio())
except ValueError as e:
    print(f"  成功捕获异常: {e}")