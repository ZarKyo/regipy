from regipy.plugins.system.timezone_data2 import TimezoneDataPlugin2
from regipy_tests.validation.validation import ValidationCase


def test_tz2_plugin_output(c: ValidationCase):
    assert c.plugin_output["\\ControlSet001\\Control\\TimeZoneInformation"] == {
        "last_write": "2012-03-11T07:00:00.000642+00:00",
        "Bias": 300,
        "DaylightBias": -60,
        "DaylightName": "@tzres.dll,-111",
        "DaylightStart": "00000300020002000000000000000000",
        "StandardBias": 0,
        "StandardName": "@tzres.dll,-112",
        "StandardStart": "00000b00010002000000000000000000",
        # TODO: Understand what happened here: utf-16 followed by garbage
        "TimeZoneKeyName": b"E\x00a\x00s\x00t\x00e\x00r\x00n\x00 \x00S\x00t\x00a\x00n\x00d\x00a\x00r\x00d\x00 \x00T\x00i\x00m\x00e\x00\x00\x00\x19ctv\x14\x06\x016\xf4\x08\xf1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x94\n\xf1\x01\xa8\n\xf1\x01\x02\x00\x00\x00\x04\x0b\xf1\x01\x00\x00\x00\x00|\x0b\xf1\x01\x00\x00\x00\x00\xc8\x0b\xf1\x01\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x07\xf1\x01\x10\xdf\t\x00\xd8qtv\xd0\x07\xf1\x01\x00\x00\x00\x00\x84\xe0\t\x00\xfb\x93sv\x02\x00\x00\x00\x00\x00\x00\x00\xe9\x8bsv\x14\x06\x016\x10\x00\x00\x00\x00 \x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\xdf\t\x00\x10\xa6\xf1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x000E\x14\x00\x14\x06\x016A\x91\x96v\xa8\n\xf1\x01/\x00\x00\x00\xd0\x07\xf1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x0e\x00\x00\x00\x10Q\x14\x00\x00\x00\x0e\x00\xa0Q\x14\x00",
        "DynamicDaylightTimeDisabled": 0,
        "ActiveTimeBias": 240,
    }


class TimezoneDataPlugin2ValidationCase(ValidationCase):
    plugin = TimezoneDataPlugin2
    test_hive_file_name = "SYSTEM.xz"
    custom_test = test_tz2_plugin_output
    expected_entries_count = 2
