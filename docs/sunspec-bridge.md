# SunSpec Bridge

[Source and full guide](https://github.com/felixsteghofer/homeassistant_sunspec-bridge) ·
[Releases](https://github.com/felixsteghofer/homeassistant_sunspec-bridge/releases) ·
[Issues](https://github.com/felixsteghofer/homeassistant_sunspec-bridge/issues)

Serves the register data from an existing SunSpec2 connection as a local Modbus
TCP endpoint for FEMS/OpenEMS. Tested with the KACO blueplanet 20.0 NX3 M2.
The domain is `fems_sunspec_bridge`; the UI name is **SunSpec Bridge**.

## Setup

1. Install/configure `hilman2/ha-sunspec2` and verify the inverter readings.
2. Add `felixsteghofer/homeassistant_sunspec-bridge` to HACS as **Integration**,
   download it, restart HA, and add **SunSpec Bridge** under Devices & services.
3. Select the SunSpec2 entry, listen address/port, unit ID, allowed client networks,
   maximum measurement age, and whether control writes should be forwarded.
4. Point FEMS/OpenEMS or its existing local forwarding rule at this listener.
   SunSpec2 must continue connecting directly to the inverter.

The source poll interval controls measurement freshness; FEMS reads cached values.
Expired readings return an exception instead of invented zeros. Supplementary
nameplate/settings reads reuse the existing session. Model 123 write forwarding
exists, but physical PV-limit control is not yet verified. New installations default
to disabled writes and localhost-only clients. The adapter uses SunSpec2 internals;
check compatibility when updating that dependency.

Existing manual installations keep their config entry and entity IDs when HACS
replaces the same domain's files. Do not delete/recreate the entry during migration.
