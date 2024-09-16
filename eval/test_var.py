"""Code for computing sample variability."""

from typing import List
import torch
from fastdtw import fastdtw
import librosa
import numpy as np
from numpy import ndarray
from scipy.spatial.distance import euclidean
from pyworld import harvest


def get_pitch(wav: ndarray, sr: int = 16000) -> ndarray:
    """Compute pitch track, removing zeros.
    Args:
        wav (ndarray): [N_sample] in (-1, 1).
        sr (int): Sampling rate.
    Returns:
        f0 (ndarray): [N_frame, 1]
    """
    x = wav.astype(np.float64)
    f0, t = harvest(x, 16000)
    f0 = f0[f0 > 10]
    return f0[:, None]


def get_mfcc(wav: ndarray, sr: int = 16000) -> ndarray:
    """Compute MFCC with fixed parameters.
    Args:
        wav (ndarray): [N_sample] in (-1, 1).
        sr (int): Sampling rate.
    Returns:
        mfcc (ndarray): [N_frame, N_MFCC].
    """
    return librosa.feature.mfcc(
        y=wav,
        sr=sr,
        n_fft=1024,
        win_length=1024,
        fmin=0,
        fmax=8000,
        n_mels=80,
        hop_length=256,
        n_mfcc=13,
        htk=True,
    ).T


def get_duration(wav: ndarray, sr: int = 16000) -> ndarray:
    raise NotImplementedError("Duration extractor not provided yet.")


def compute_avg_dist(seqs: List[ndarray]) -> float:
    """Compute average DTW distances between sequences.
    Args:
        seqs (List[ndarray]): List of [N_step, D] sequences.
    Returns:
        avg_dist (float).
    """
    res = 0.0
    cnt = 0
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i <= j:
                continue
            A, B = seqs[i], seqs[j]
            D, P = fastdtw(A, B, dist=euclidean)
            res = res * (cnt / (cnt + 1)) + D / (cnt + 1)
            cnt += 1
            print(f"{cnt:04d} {D / len(P):4.2f} {res:4.2f}", end="\r")
    return res
