"""A nendo plugin for audio effects mostly based on pedalboard by Spotify's Audio Intelligence Lab."""
from logging import Logger
from typing import Any, Optional, Tuple

import numpy as np
import pedalboard
from nendo import Nendo, NendoConfig, NendoEffectPlugin
from pedalboard import (
    Chorus,
    Compressor,
    Delay,
    Distortion,
    HighShelfFilter,
    HighpassFilter,
    Limiter,
    LowShelfFilter,
    LowpassFilter,
    Pedalboard,
    Phaser,
    Reverb,
)


class NendoFxCore(NendoEffectPlugin):
    """A nendo plugin for audio effects mostly based on pedalboard by Spotify's Audio Intelligence Lab.

    Attributes:
        nendo_instance (Nendo): The instance of Nendo using this plugin.
        config (NendoConfig): The configuration of the Nendo instance.
        logger (Logger): The logger to use for reporting.
        board (Pedalboard): The pedalboard instance to use for chaining effects.

    Examples:
        ```python
        from nendo import Nendo, NendoConfig

        nendo = Nendo(config=NendoConfig(plugins=["nendo_plugin_fx_core"]))
        track = nendo.library.add_track_from_file(
            file_path="path/to/file.wav",
        )

        # add reverb
        reverb_track = nendo.plugins.fx_core.reverb(
            track=track,
            wet_level=0.2,
            dry_level=0.8,
            room_size=0.1,
        )
        reverb_track.play()
        ```
    """

    nendo_instance: Nendo = None
    config: NendoConfig = None
    logger: Logger = None
    board: Pedalboard = None

    def __init__(self, **data: Any):
        """Initialize the plugin."""
        super().__init__(**data)
        self.board = Pedalboard()

    @NendoEffectPlugin.run_signal
    def reverb(
        self,
        signal: np.ndarray,
        sr: int,
        wet_level: float = 0.2,
        dry_level: float = 0.8,
        room_size: float = 0.1,
        damping: float = 0.7,
        width: float = 1.0,
        freeze_mode: float = 0.0,
    ) -> Tuple[np.ndarray, int]:
        """Add a reverb effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            wet_level (float, optional): The wet level of the reverb. Defaults to 0.2.
            dry_level (float, optional): The dry level of the reverb. Defaults to 0.8.
            room_size (float, optional): The room size of the reverb. Defaults to 0.1.
            damping (float, optional): The damping of the reverb. Defaults to 0.7.
            width (float, optional): The width of the reverb. Defaults to 1.0.
            freeze_mode (float, optional): The freeze mode of the reverb. Defaults to 0.0.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        reverb = Reverb(
            wet_level=wet_level,
            dry_level=dry_level,
            room_size=room_size,
            damping=damping,
            width=width,
            freeze_mode=freeze_mode,
        )
        return self._append_and_run(reverb, signal, sr)

    @NendoEffectPlugin.run_signal
    def distortion(
        self,
        signal: np.ndarray,
        sr: int,
        drive_db: float = 25.0,
    ) -> Tuple[np.ndarray, int]:
        """Add a distortion effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            drive_db (float, optional): The drive of the distortion. Defaults to 25.0.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        distortion = Distortion(drive_db=drive_db)
        return self._append_and_run(distortion, signal, sr)

    @NendoEffectPlugin.run_signal
    def phaser(
        self,
        signal: np.ndarray,
        sr: int,
        rate_hz: float = 1.0,
        depth: float = 0.5,
        centre_frequency_hz: float = 1300.0,
        feedback: float = 0.0,
        mix: float = 0.5,
    ) -> Tuple[np.ndarray, int]:
        """Add a phaser effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            rate_hz (float, optional): The rate of the phaser. Defaults to 1.0.
            depth (float, optional): The depth of the phaser. Defaults to 0.5.
            centre_frequency_hz (float, optional): The centre frequency of the phaser. Defaults to 1300.0.
            feedback (float, optional): The feedback of the phaser. Defaults to 0.0.
            mix (float, optional): The mix of the phaser. Defaults to 0.5.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        phaser = Phaser(
            rate_hz=rate_hz,
            depth=depth,
            centre_frequency_hz=centre_frequency_hz,
            feedback=feedback,
            mix=mix,
        )
        return self._append_and_run(phaser, signal, sr)

    @NendoEffectPlugin.run_signal
    def delay(
        self,
        signal: np.ndarray,
        sr: int,
        delay_seconds: float = 0.5,
        feedback: float = 0.0,
        mix: float = 0.5,
    ) -> Tuple[np.ndarray, int]:
        """Add a delay effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            delay_seconds (float, optional): The delay in seconds. Defaults to 0.5.
            feedback (float, optional): The feedback of the delay. Defaults to 0.0.
            mix (float, optional): The mix of the delay. Defaults to 0.5.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        delay = Delay(delay_seconds=delay_seconds, feedback=feedback, mix=mix)
        return self._append_and_run(delay, signal, sr)

    @NendoEffectPlugin.run_signal
    def chorus(
        self,
        signal: np.ndarray,
        sr: int,
        rate_hz: float = 1.0,
        depth: float = 0.25,
        centre_delay_ms: float = 7.0,
        feedback: float = 0.0,
        mix: float = 0.5,
    ) -> Tuple[np.ndarray, int]:
        """Add a chorus effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            rate_hz (float, optional): The rate of the chorus. Defaults to 1.0.
            depth (float, optional): The depth of the chorus. Defaults to 0.25.
            centre_delay_ms (float, optional): The centre delay in milliseconds. Defaults to 7.0.
            feedback (float, optional): The feedback of the chorus. Defaults to 0.0.
            mix (float, optional): The mix of the chorus. Defaults to 0.5.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        chorus = Chorus(
            rate_hz=rate_hz,
            depth=depth,
            centre_delay_ms=centre_delay_ms,
            feedback=feedback,
            mix=mix,
        )
        return self._append_and_run(chorus, signal, sr)

    @NendoEffectPlugin.run_signal
    def compressor(
        self,
        signal: np.ndarray,
        sr: int,
        threshold_db: float = 0,
        ratio: float = 1,
        attack_ms: float = 1.0,
        release_ms: float = 100,
    ) -> Tuple[np.ndarray, int]:
        """Add a compressor effect to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            threshold_db (float, optional): The threshold in decibels. Defaults to 0.
            ratio (float, optional): The ratio. Defaults to 1.
            attack_ms (float, optional): The attack in milliseconds. Defaults to 1.0.
            release_ms (float, optional): The release in milliseconds. Defaults to 100.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        compressor = Compressor(
            threshold_db=threshold_db,
            ratio=ratio,
            attack_ms=attack_ms,
            release_ms=release_ms,
        )
        return self._append_and_run(compressor, signal, sr)

    @NendoEffectPlugin.run_signal
    def stereo(self, signal: np.ndarray, sr: int) -> Tuple[np.ndarray, int]:
        """Convert a mono signal to stereo using the Haas effect.

        https://en.wikipedia.org/wiki/Precedence_effect

        When given a stereo signal the function will just return the original signal.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        if signal.ndim == 1:
            signal = np.stack([signal, signal])
        elif signal.shape[0] == 1:
            signal = np.repeat(signal, 2, axis=0)

        # ignore already stereo signals
        elif np.array_equal(signal[0], signal[1]):
            return signal, sr

        delay_offset = int(sr * 0.15)  # 15 ms
        haas_signal = np.roll(signal, shift=delay_offset, axis=0)
        haas_signal[0, :delay_offset] = 0.0
        haas_signal[0, :] *= -1

        return haas_signal, sr

    @NendoEffectPlugin.run_signal
    def limiter(
        self,
        signal: np.ndarray,
        sr: int,
        release_ms: Optional[float] = 100,
        threshold_db: Optional[float] = None,
    ) -> Tuple[np.ndarray, int]:
        """Apply a limiter to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            release_ms (Optional[float], optional): The release in milliseconds. Defaults to 100.
            threshold_db (Optional[float], optional): The threshold in decibels. Defaults to None.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        limiter = Limiter(release_ms=release_ms)

        # adaptive limiting
        if threshold_db is None:
            peak_amp = np.max(20 * np.log10(np.abs(signal)))
            threshold = peak_amp - 0.1
            limiter.threshold_db = threshold
        else:
            limiter.threshold_db = threshold_db

        return self._append_and_run(limiter, signal, sr)

    @NendoEffectPlugin.run_signal
    def highpass(
        self,
        signal: np.ndarray,
        sr: int,
        cutoff_frequency_hz: Optional[float] = 50,
    ):
        """Apply a highpass filter to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            cutoff_frequency_hz (Optional[float], optional): The cutoff frequency in hertz. Defaults to 50.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        eq = HighpassFilter(cutoff_frequency_hz=cutoff_frequency_hz)
        return self._append_and_run(eq, signal, sr)

    @NendoEffectPlugin.run_signal
    def lowpass(
        self,
        signal: np.ndarray,
        sr: int,
        cutoff_frequency_hz: Optional[float] = 50,
    ):
        """Apply a lowpass filter to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            cutoff_frequency_hz (Optional[float], optional): The cutoff frequency in hertz. Defaults to 50.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        eq = LowpassFilter(cutoff_frequency_hz=cutoff_frequency_hz)
        return self._append_and_run(eq, signal, sr)

    @NendoEffectPlugin.run_signal
    def low_shelf(
        self,
        signal: np.ndarray,
        sr: int,
        cutoff_frequency_hz: Optional[float] = 50,
        gain_db: Optional[float] = 0.0,
        q: Optional[float] = 0.7071067690849304,
    ):
        """Apply a low shelf filter to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            cutoff_frequency_hz (Optional[float], optional): The cutoff frequency in hertz. Defaults to 50.
            gain_db (Optional[float], optional): The gain in decibels. Defaults to 0.0.
            q (Optional[float], optional): The q factor. Defaults to 0.7071067690849304.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        eq = LowShelfFilter(
            cutoff_frequency_hz=cutoff_frequency_hz,
            gain_db=gain_db,
            q=q,
        )
        return self._append_and_run(eq, signal, sr)

    @NendoEffectPlugin.run_signal
    def high_shelf(
        self,
        signal: np.ndarray,
        sr: int,
        cutoff_frequency_hz: Optional[float] = 50,
        gain_db: Optional[float] = 0.0,
        q: Optional[float] = 0.7071067690849304,
    ):
        """Apply a high shelf filter to a track or a collection.

        Args:
            signal (np.ndarray): The audio signal to process.
            sr (int): The sample rate of the audio signal.
            cutoff_frequency_hz (Optional[float], optional): The cutoff frequency in hertz. Defaults to 50.
            gain_db (Optional[float], optional): The gain in decibels. Defaults to 0.0.
            q (Optional[float], optional): The q factor. Defaults to 0.7071067690849304.

        Returns:
            Tuple[np.ndarray, int]: The processed audio signal and the sample rate.
        """
        eq = HighShelfFilter(
            cutoff_frequency_hz=cutoff_frequency_hz,
            gain_db=gain_db,
            q=q,
        )
        return self._append_and_run(eq, signal, sr)

    def _append_and_run(
        self,
        effect: pedalboard.Plugin,
        signal: np.ndarray,
        sr: int,
    ) -> Tuple[np.ndarray, int]:
        """Append an effect to the pedalboard and run it on the signal."""
        self.board.append(effect)
        output_audio = self.board(input_array=signal, sample_rate=sr)
        self.board.reset()
        return output_audio, sr
