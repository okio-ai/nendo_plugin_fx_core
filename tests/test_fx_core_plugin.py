# -*- encoding: utf-8 -*-
"""Tests for the Nendo FxCore plugin."""
import unittest

from nendo import Nendo, NendoConfig, NendoError

nd = Nendo(
    config=NendoConfig(
        library_path="./library",
        log_level="INFO",
        plugins=["nendo_plugin_fx_core"],
    )
)


class FxCorePluginTest(unittest.TestCase):
    def test_run_reverb(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        reverb_track = nd.plugins.fx_core.reverb(
            track=track,
        )
        self.assertEqual(reverb_track.sr, track.sr)

    def test_run_process_reverb_throws_exception(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")
        self.assertRaises(NendoError, track.process, "nendo_plugin_fx_core")

    def test_run_process_reverb_collection_throws_exception(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")
        collection = nd.library.add_collection(
            name="test_collection",
            track_ids=[track.id],
        )
        self.assertRaises(NendoError, collection.process, "nendo_plugin_fx_core")

    def test_run_distortion(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        distortion_track = nd.plugins.fx_core.distortion(
            track=track,
        )
        self.assertEqual(distortion_track.sr, track.sr)

    def test_run_chorus(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        chorus_track = nd.plugins.fx_core.chorus(
            track=track,
        )
        self.assertEqual(chorus_track.sr, track.sr)

    def test_run_phaser(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        phaser_track = nd.plugins.fx_core.phaser(
            track=track,
        )
        self.assertEqual(phaser_track.sr, track.sr)

    def test_run_delay(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        delay_track = nd.plugins.fx_core.delay(
            track=track,
        )
        self.assertEqual(delay_track.sr, track.sr)

    def test_run_compressor(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        compressor_track = nd.plugins.fx_core.compressor(
            track=track,
        )
        self.assertEqual(compressor_track.sr, track.sr)

    def test_run_stereo(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        stereo_track = nd.plugins.fx_core.stereo(
            track=track,
        )
        self.assertEqual(stereo_track.sr, track.sr)

    def test_run_limiter(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        limiter_track = nd.plugins.fx_core.limiter(
            track=track,
        )
        self.assertEqual(limiter_track.sr, track.sr)

    def test_run_highpass(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        highpass_track = nd.plugins.fx_core.highpass(
            track=track,
        )
        self.assertEqual(highpass_track.sr, track.sr)

    def test_run_lowpass(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        lowpass_track = nd.plugins.fx_core.lowpass(
            track=track,
        )
        self.assertEqual(lowpass_track.sr, track.sr)

    def test_run_low_shelf(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        low_shelf_track = nd.plugins.fx_core.low_shelf(
            track=track,
        )
        self.assertEqual(low_shelf_track.sr, track.sr)

    def test_run_high_shelf(self):
        nd.library.reset(force=True)
        track = nd.library.add_track(file_path="tests/assets/test.wav")

        high_shelf_track = nd.plugins.fx_core.high_shelf(
            track=track,
        )
        self.assertEqual(high_shelf_track.sr, track.sr)


if __name__ == "__main__":
    unittest.main()
