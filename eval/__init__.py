import torch
from torch import Tensor


def audio_standardize(
    src_path: str,
    target_sr: int = 16000,
    target_loudness: float = -25.0,
) -> Tensor:
    """For all evaluations, we normalize and downsample the waveforms with this function."""
    import soundfile as sf
    import pyloudnorm as pyln
    from librosa import resample

    if audio_standardize.meter is None:
        audio_standardize.meter = pyln.Meter(target_sr)  # create BS.1770 meter
    meter = audio_standardize.meter

    src_wave, src_rate = sf.read(src_path)
    tgt_wave = resample(src_wave, orig_sr=src_rate, target_sr=target_sr)
    loudness = meter.integrated_loudness(tgt_wave)
    tgt_wave = pyln.normalize.loudness(tgt_wave, loudness, target_loudness)
    tgt_wave = torch.as_tensor(tgt_wave).float()
    return tgt_wave
