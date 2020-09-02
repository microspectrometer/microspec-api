import microspec as usp
import pytest

class TestCommandGetBridgeLED():
    def test_Call_getBridgeLED_with_optional_param_led_num(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.getBridgeLED(led_num=0).status == 'OK'
        assert kit.getBridgeLED(0).status == 'OK'
    def test_Call_getBridgeLED_without_optional_param_led_num(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.getBridgeLED().status == 'OK'
    def test_Call_getBridgeLED_with_an_invalid_led_num_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        invalid_led_num = 1
        assert kit.getBridgeLED(invalid_led_num).status == 'ERROR'
    def test_getBridgeLED_returns_str_OFF_GREEN_or_RED(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        led = kit.getBridgeLED().led_setting
        assert (
            led is 'OFF' or
            led is 'GREEN' or
            led is 'RED'
            )

class TestCommandSetBridgeLED():
    def test_Call_setBridgeLED_with_optional_param_led_num(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.setBridgeLED(led_num=0, led_setting=usp.GREEN).status == 'OK'
        assert kit.setBridgeLED(usp.GREEN, led_num=0).status == 'OK'
        assert kit.setBridgeLED(usp.GREEN, 0).status == 'OK'
    def test_Call_setBridgeLED_without_optional_param_led_num(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.setBridgeLED(usp.GREEN).status == 'OK'
    def test_Call_setBridgeLED_with_an_invalid_led_num_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        invalid_led_num = 1
        assert kit.setBridgeLED(usp.GREEN, invalid_led_num).status == 'ERROR'
    def test_Call_setBridgeLED_without_required_param_led_setting_raises_TypeError(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        with pytest.raises(TypeError):
            kit.setBridgeLED()
    def test_Call_setBridgeLED_with_invalid_led_setting_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        invalid_led_setting = 3
        assert kit.setBridgeLED(invalid_led_setting).status == 'ERROR'
    def test_Call_setBridgeLED(self, devkit_connection):
        kit = devkit_connection
        assert kit.setBridgeLED(usp.OFF).status == 'OK'
        assert kit.setBridgeLED(usp.GREEN).status == 'OK'
        assert kit.setBridgeLED(usp.RED).status == 'OK'
        # cleanup
        kit.setBridgeLED(usp.GREEN)

class TestCommandGetSensorLED():
    def test_Call_getSensorLED(self, devkit_connection):
        kit = devkit_connection
        assert kit.getSensorLED(led_num=0).status == 'OK'
        assert kit.getSensorLED(0).status == 'OK'
        assert kit.getSensorLED(1).status == 'OK'
    def test_Call_getSensorLED_with_invalid_led_num_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        invalid_led_num = 2
        assert kit.getSensorLED(led_num=2).status == 'ERROR'
    def test_Call_getSensorLED_without_required_param_led_num_raises_TypeError(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        with pytest.raises(TypeError):
            kit.getSensorLED()

    def test_getSensorLED_returns_str_OFF_GREEN_or_RED(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        led0 = kit.getSensorLED(0).led_setting
        led1 = kit.getSensorLED(1).led_setting
        assert (
            led0 is 'OFF' or
            led0 is 'GREEN' or
            led0 is 'RED'
            )
        assert (
            led1 is 'OFF' or
            led1 is 'GREEN' or
            led1 is 'RED'
            )
    def test_getSensorLED_always_returns_str_OFF_for_LED0(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        led0 = kit.getSensorLED(0).led_setting
        assert led0 is 'OFF'

class TestCommandSetSensorLED():
    def test_Call_setSensorLED_without_led_num_raises_TypeError(self, devkit_connection):
        kit = devkit_connection
        with pytest.raises(TypeError):
            kit.setSensorLED(led_setting=usp.GREEN)
    def test_Call_setSensorLED_without_led_setting_raises_TypeError(self, devkit_connection):
        kit = devkit_connection
        with pytest.raises(TypeError):
            kit.setSensorLED(led_num=0)
    def test_Call_setSensorLED(self, devkit_connection):
        kit = devkit_connection
        state = usp.RED;
        lednum = 0
        assert kit.setSensorLED(usp.OFF, lednum).status == 'OK'
        assert kit.setSensorLED(usp.GREEN, lednum).status == 'OK'
        assert kit.setSensorLED(usp.RED, lednum).status == 'OK'
        lednum = 1
        assert kit.setSensorLED(usp.OFF, lednum).status == 'OK'
        assert kit.setSensorLED(usp.GREEN, lednum).status == 'OK'
        assert kit.setSensorLED(usp.RED, lednum).status == 'OK'
        # cleanup
        kit.setSensorLED(usp.GREEN, 0)
        kit.setSensorLED(usp.GREEN, 1)

class TestCommandGetSensorConfig():
    def test_getSensorConfig_returns_OK(self, devkit_connection):
        kit = devkit_connection
        assert kit.getSensorConfig().status == 'OK'
    def test_getSensorConfig_returns_BINNING_ON_or_BINNING_OFF(self, devkit_connection):
        kit = devkit_connection
        binning = kit.getSensorConfig().binning
        assert binning is 'BINNING_ON' or binning is 'BINNING_OFF'
    def test_getSensorConfig_returns_gain_1X_2point5X_4X_or_5X(self, devkit_connection):
        kit = devkit_connection
        gain = kit.getSensorConfig().gain
        assert (
            gain is 'GAIN1X' or
            gain is 'GAIN2_5X' or
            gain is 'GAIN4X' or
            gain is 'GAIN5X'
            )
    def test_getSensorConfig_returns_str_ALL_ROWS_if_row_bitmap_is_0x1F(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        row_bitmap = kit.getSensorConfig().row_bitmap
        assert row_bitmap is 'ALL_ROWS'
    def test_getSensorConfig_returns_int_row_bitmap_if_row_bitmap_is_not_0x1F(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        ROWS123 = 0x05
        kit.setSensorConfig(row_bitmap=ROWS123)
        row_bitmap = kit.getSensorConfig().row_bitmap
        assert row_bitmap == ROWS123

class TestCommandSetSensorConfig():
    def test_setSensorConfig_default_params_are_BINNING_ON_GAIN1X_and_ALL_ROWS(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        kit.setSensorConfig()
        assert kit.getSensorConfig().binning == 'BINNING_ON'
        assert kit.getSensorConfig().gain == 'GAIN1X'
        assert kit.getSensorConfig().row_bitmap == 'ALL_ROWS'
    def test_Call_setSensorConfig_with_invalid_binning_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.setSensorConfig(binning=2).status == 'ERROR'
    def test_Call_setSensorConfig_with_invalid_gain_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.setSensorConfig(gain=2).status == 'ERROR'
    def test_Call_setSensorConfig_with_invalid_row_bitmap_returns_ERROR(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        # row_bitmap is invalid if three most-significant bits are set
        assert kit.setSensorConfig(row_bitmap=0xE0).status == 'ERROR'
        assert kit.setSensorConfig(row_bitmap=0xFF).status == 'ERROR'
    def test_Call_setSensorConfig_with_row_bitmap_0x00_returns_OK(
            self,
            devkit_connection
            ):
        kit = devkit_connection
        assert kit.setSensorConfig(row_bitmap=0x00).status == 'OK'
        assert kit.getSensorConfig().row_bitmap == 0x00
    def test_Call_setSensorConfig(self, devkit_connection):
        kit = devkit_connection
        assert kit.setSensorConfig(
                usp.BINNING_ON,
                usp.GAIN1X,
                usp.ALL_ROWS
                ).status == 'OK'
        # cleanup
        kit.setSensorConfig() # call with default values
        default_config = kit.getSensorConfig()
        assert default_config.binning == 'BINNING_ON'
        assert default_config.gain == 'GAIN1X'
        assert default_config.row_bitmap == 'ALL_ROWS'
