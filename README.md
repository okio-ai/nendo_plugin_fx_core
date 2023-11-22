# Nendo Plugin FX Core

<br>
<p align="left">
    <img src="https://okio.ai/docs/assets/nendo_core_logo.png" width="350" alt="Nendo Core">
</p>
<br>

---

![Documentation](https://img.shields.io/website/https/nendo.ai)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/okio_ai.svg?style=social&label=Follow%20%40okio_ai)](https://twitter.com/okio_ai) [![](https://dcbadge.vercel.app/api/server/XpkUsjwXTp?compact=true&style=flat)](https://discord.gg/XpkUsjwXTp)

NendoFX: Use common audio effects out of the box (based on [pedalboard](https://github.com/spotify/pedalboard) by Spotify Research).

## Features

- Apply well known audio effects to a `NendoTrack`
- modulation via: `chorus`, `phaser`
- different filters: `lowpass`, `highpass`, `low_shelf`, `high_shelf`
- adaptive processing based on MIR features via: `limiter`
- custom effects like: `stereo`
- also basics like: `distortion`, `reverb`, `delay`, `compressor`

## Installation

1. [Install Nendo](https://github.com/okio-ai/nendo#installation)
2. `pip install nendo-plugin-fx-core`

## Usage

Take a look at a basic usage example below.
For more detailed information, please refer to the [documentation](https://okio.ai/docs/plugins).

For more advanced examples, check out the examples folder.
or try it in colab:

<a target="_blank" href="https://colab.research.google.com/drive/1wSGM2lhgP1z8gL2cVOErzot9m9AJ1zCU?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```python
from nendo import Nendo, NendoConfig

nd = Nendo(config=NendoConfig(plugins=["nendo_plugin_fx_core"]))

track = nd.library.add_track(file_path='/path/to/track.mp3')


track = nd.plugins.fx_core.compressor(track)
track = nd.plugins.fx_core.reverb(
    track=track,
    wet_level=0.2,
    dry_level=0.8,
    room_size=0.1,
)
track = nd.plugins.fx_core.limiter(track)
track.play()
```

## Contributing

Visit our docs to learn all about how to contribute to Nendo: [Contributing](https://okio.ai/docs/contributing/)

## Licence

Nendo: MIT

Pedalboard: GPL3

For additional licences check https://github.com/spotify/pedalboard