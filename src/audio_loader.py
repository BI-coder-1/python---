import os
import numpy as np
from scipy.io import wavfile
class AudioSample:
    def __init__(self,filepath,sample_rate,data):
        self.filepath = filepath
        self.sample_rate = sample_rate
        self.data = data
        if len(data.shape)==1:
            self.channels = 1
            self.num_samples = data.shape[0]
        else:
            self.channels = data.shape[1]
            self.num_samples = data.shape[0]
        self.duration = self.num_samples / self.sample_rate
    def __str__(self):
        """打印这个对象时自动调用的方法，输出格式化的信息"""
        info = f"文件名: {os.path.basename(self.filepath)}\n"
        info += f"采样率: {self.sample_rate} Hz\n"
        info += f"声道数: {self.channels}\n"
        info += f"采样点数: {self.num_samples}\n"
        info += f"音频时长: {self.duration:.2f} 秒\n"
        info += f"原始数据类型: {self.data.dtype}\n"
        info += f"归一化后幅度范围: [{np.min(self.data):.4f}, {np.max(self.data):.4f}]\n"
        return info
def load_wav(filepath):
        """
        读取 WAV 文件，并返回 AudioSample 对象。
        包含文件存在性检查、格式检查和归一化处理。
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"找不到文件: {filepath}")
        if not filepath.lower().endswith('.wav'):
            raise ValueError(f"文件格式错误，仅支持 .wav 文件: {filepath}")
        try:
            sample_rate, raw_data = wavfile.read(filepath)
        except Exception as e:
            raise ValueError(f"读取音频失败，可能是文件损坏或格式不支持。详细错误: {e}")
        if np.issubdtype(raw_data.dtype, np.integer):
            max_val=np.iinfo(raw_data.dtype).max
            normalized_data=raw_data.astype(np.float32) / max_val
        else:
            normalized_data = raw_data.astype(np.float32)
        # 5. 返回封装好的对象
        return AudioSample(filepath, sample_rate, normalized_data)