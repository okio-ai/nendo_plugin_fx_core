# Advanced Usage

Below you can see all currently supported effects with their parameters.
For detailed explanations of the algorithms used for each effect, 
please refer to the official [pedalboard documentation](https://spotify.github.io/pedalboard/reference/pedalboard.html#).

### Reverb

| Parameter   | Type       | Description                          | Default Value |
|-------------|------------|--------------------------------------|---------------|
| wet_level   | float      | The wet level of the reverb.         | 0.2           |
| dry_level   | float      | The dry level of the reverb.         | 0.8           |
| room_size   | float      | The room size of the reverb.         | 0.1           |
| damping     | float      | The damping of the reverb.           | 0.7           |
| width       | float      | The width of the reverb.             | 1.0           |
| freeze_mode | float      | The freeze mode of the reverb.       | 0.0           |

### Distortion

| Parameter | Type       | Description                          | Default Value |
|-----------|------------|--------------------------------------|---------------|
| drive_db  | float      | The drive of the distortion.         | 25.0          |

### Phaser

| Parameter           | Type       | Description                          | Default Value |
|---------------------|------------|--------------------------------------|---------------|
| rate_hz             | float      | The rate of the phaser.              | 1.0           |
| depth               | float      | The depth of the phaser.             | 0.5           |
| centre_frequency_hz | float      | The centre frequency of the phaser.  | 1300.0        |
| feedback            | float      | The feedback of the phaser.          | 0.0           |
| mix                 | float      | The mix of the phaser.               | 0.5           |

### Delay

| Parameter     | Type       | Description                          | Default Value |
|---------------|------------|--------------------------------------|---------------|
| delay_seconds | float      | The delay in seconds.                | 0.5           |
| feedback      | float      | The feedback of the delay.           | 0.0           |
| mix           | float      | The mix of the delay.                | 0.5           |

### Chorus

| Parameter       | Type       | Description                          | Default Value |
|-----------------|------------|--------------------------------------|---------------|
| rate_hz         | float      | The rate of the chorus.              | 1.0           |
| depth           | float      | The depth of the chorus.             | 0.25          |
| centre_delay_ms | float      | The centre delay in milliseconds.    | 7.0           |
| feedback        | float      | The feedback of the chorus.          | 0.0           |
| mix             | float      | The mix of the chorus.               | 0.5           |

### Compressor

| Parameter    | Type       | Description                          | Default Value |
|--------------|------------|--------------------------------------|---------------|
| threshold_db | float      | The threshold in decibels.           | 0             |
| ratio        | float      | The ratio.                           | 1             |
| attack_ms    | float      | The attack in milliseconds.          | 1.0           |
| release_ms   | float      | The release in milliseconds.         | 100           |

### Stereo

This plugin creates a stereo signal from a mono signal by using the Haas effect.

### Limiter

If no `threshold_db` is given, the threshold is calculated based on MIR features of the track.

| Parameter    | Type            | Description                          | Default Value |
|--------------|-----------------|--------------------------------------|---------------|
| release_ms   | Optional[float] | The release in milliseconds.         | 100           |
| threshold_db | Optional[float] | The threshold in decibels.           | None          |

### Highpass

| Parameter           | Type            | Description                          | Default Value |
|---------------------|-----------------|--------------------------------------|---------------|
| cutoff_frequency_hz | Optional[float] | The cutoff frequency in hertz.       | 50            |

### Lowpass

| Parameter           | Type            | Description                          | Default Value |
|---------------------|-----------------|--------------------------------------|---------------|
| cutoff_frequency_hz | Optional[float] | The cutoff frequency in hertz.       | 50            |

### Low Shelf

| Parameter           | Type            | Description                          | Default Value      |
|---------------------|-----------------|--------------------------------------|--------------------|
| cutoff_frequency_hz | Optional[float] | The cutoff frequency in hertz.       | 50                 |
| gain_db             | Optional[float] | The gain in decibels.                | 0.0                |
| q                   | Optional[float] | The q factor.                        | 0.7071067690849304 |

### High Shelf

| Parameter           | Type            | Description                          | Default Value      |
|---------------------|-----------------|--------------------------------------|--------------------|
| cutoff_frequency_hz | Optional[float] | The cutoff frequency in hertz.       | 50                 |
| gain_db             | Optional[float] | The gain in decibels.                | 0.0                |
| q                   | Optional[float] | The q factor.                        | 0.7071067690849304 |