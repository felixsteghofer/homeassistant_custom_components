# Home Assistant custom components

[Home Assistant](https://home-assistant.io/)

## Shinobi

[Shinobi](https://shinobi.video/) is an open source cctv solution. 

To enable this component, first copy `custom_components/` inside your Home Assistant config directory and add the Shinobi component and platform, for example in `configuration.yaml`. See https://github.com/moeiscool/Shinobi/wiki/API-Access on how to get your `api_key` and `group_key`. The `ssl` param is optional and defaults to `false`. The white- and blacklist is also optional and defaults to all active monitors. It can also be only one filtering method applied. For now, the name assigned in Shinobi is used to filter cams.

```
…
shinobi:
  host: <your-cams_ip or hostname>
  api_key: <api_key>
  group_key: <group_key>
  ssl: false

camera:
  - platform: shinobi
    whitelist: 
      - cam0_name
    blacklist: 
      - cam1_name
      - cam2_name
…
```

At the moment, all configured and activated cameras (in state, `Record` or `Watch-only`, see https://shinobi.video/docs/settings) are fetched and added to Home Assistant as `MjpegCamera`. Please note that I couldn't get the actual Mjpeg stream to work in general using other software so this is also not working in HA for now. The preview with still images is working perfectly though.

No additional packages have to be installed.

## TODO

- get the (mjpeg-) stream to work, also figure out which camera platform is working best for this (Shinobi allows to switch between different stream output configs)
- allow filtering of which monitors/cams to add to HA
- add movement detection as (binary?) sensors
- add ptz control (as switches? I have not yet seen a good solution in HA, anybody who can help please drop some lines)
- …
