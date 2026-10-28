import numpy as np
def extract_basic_features(audio):
    """
    接受AudioSample对象，计算并返回包含各项基础时域的特征
    """
    data=audio.data.astype(np.float64)
    if len(data)==0:
        raise ValueError("has no data")
    if len(data.shape)>1:
        data=np.mean(data,axis=1)
    min_amp=np.min(data) #最小幅度
    max_amp=np.max(data)
    peak_amp=np.max(np.abs(data)) #峰值幅度
    mean_val=np.mean(data) #平均
    mean_abs_amp=np.mean(np.abs(data)) #绝对平均
    total_energy=np.sum(np.square(data)) #总能量
    avg_energy=np.mean(np.square(data)) #平均能量
    rms=np.sqrt(avg_energy)
    return {
        "min_amplitude": float(min_amp),
        "max_amplitude": float(max_amp),
        "peak_amplitude": float(peak_amp),
        "mean": float(mean_val),
        "mean_absolute_amplitude": float(mean_abs_amp),
        "total_energy": float(total_energy),
        "average_energy": float(avg_energy),
        "rms": float(rms)
    }