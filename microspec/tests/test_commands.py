import microspec as usp
import pytest

class TestCommandGetBridgeLED():
    def test_Call_getBridgeLED_using_default_for_param_led_num(self, kit):
        assert kit.getBridgeLED().status == 'OK'
    def test_Call_getBridgeLED_specifying_param_led_num(self, kit):
        assert kit.getBridgeLED(0).status == 'OK'
    def test_Call_getBridgeLED_specifying_param_led_num_by_keyword(self, kit):
        assert kit.getBridgeLED(led_num=0).status == 'OK'
    def test_getBridgeLED_Returns_str_OFF_str_GREEN_or_str_RED(self, kit):
        led = kit.getBridgeLED().led_setting
        assert (
            led == 'OFF' or
            led == 'GREEN' or
            led == 'RED'
            )
    def test_getBridgeLED_Returns_ERROR_if_param_led_num_is_invalid(self, kit):
        invalid_led_num = 1
        assert kit.getBridgeLED(invalid_led_num).status == 'ERROR'

class TestCommandSetBridgeLED():
    def test_Call_setBridgeLED_using_default_for_param_led_num(self, kit):
        assert kit.setBridgeLED(usp.GREEN).status == 'OK'
    def test_Call_setBridgeLED_specifying_param_led_num(self, kit):
        assert kit.setBridgeLED(usp.GREEN, 0).status == 'OK'
    def test_Call_setBridgeLED_specifying_param_led_num_by_keyword(self, kit):
        assert kit.setBridgeLED(usp.GREEN, led_num=0).status == 'OK'
    def test_Call_setBridgeLED_specifying_all_params_by_keyword(self, kit):
        assert kit.setBridgeLED(led_num=0, led_setting=usp.GREEN).status == 'OK'
    def test_setBridgeLED_Returns_ERROR_if_param_led_num_is_invalid(self, kit):
        invalid_led_num = 1
        assert kit.setBridgeLED(usp.GREEN, invalid_led_num).status == 'ERROR'
    def test_setBridgeLED_Raises_TypeError_if_param_led_setting_is_missing(self, kit):
        with pytest.raises(TypeError):
            kit.setBridgeLED()
    def test_setBridgeLED_Returns_ERROR_if_param_led_setting_is_invalid(self, kit):
        invalid_led_setting = 3
        assert kit.setBridgeLED(invalid_led_setting).status == 'ERROR'
    def test_See_these_examples_for_setBridgeLED(self, kit):
        assert kit.setBridgeLED(usp.OFF).status == 'OK'
        assert kit.setBridgeLED(usp.GREEN).status == 'OK'
        assert kit.setBridgeLED(usp.RED).status == 'OK'
    def test_Restore_the_Bridge_LED_to_its_default_state(self, kit):
        kit.setBridgeLED(usp.GREEN)

class TestCommandGetSensorLED():
    def test_Call_getSensorLED_specifying_param_led_num(self, kit):
        assert kit.getSensorLED(0).status == 'OK'
        assert kit.getSensorLED(1).status == 'OK'
    def test_Call_getSensorLED_specifying_param_led_num_by_keyword(self, kit):
        assert kit.getSensorLED(led_num=0).status == 'OK'
        assert kit.getSensorLED(led_num=1).status == 'OK'
    def test_getSensorLED_Returns_ERROR_if_led_num_is_invalid(self, kit):
        invalid_led_num = 2
        assert kit.getSensorLED(led_num=2).status == 'ERROR'
    def test_getSensorLED_Raises_TypeError_if_param_led_num_is_missing(self, kit):
        with pytest.raises(TypeError):
            kit.getSensorLED()
    def test_getSensorLED_Returns_str_OFF_str_GREEN_or_str_RED(self, kit):
        led0 = kit.getSensorLED(0).led_setting
        led1 = kit.getSensorLED(1).led_setting
        assert (
            led0 == 'OFF' or
            led0 == 'GREEN' or
            led0 == 'RED'
            )
        assert (
            led1 == 'OFF' or
            led1 == 'GREEN' or
            led1 == 'RED'
            )
    def test_getSensorLED_Always_returns_str_OFF_for_LED0(self, kit):
        led0 = kit.getSensorLED(0).led_setting
        assert led0 == 'OFF'

class TestCommandSetSensorLED():
    def test_Call_setSensorLED_specifying_params_by_position(self, kit):
        assert kit.setSensorLED(usp.RED, 0).status == 'OK'
        assert kit.setSensorLED(usp.RED, 1).status == 'OK'
    def test_Call_setSensorLED_specifying_params_by_keyword(self, kit):
        assert kit.setSensorLED(led_setting=usp.RED, led_num=0).status == 'OK'
        assert kit.setSensorLED(led_setting=usp.RED, led_num=1).status == 'OK'
    def test_setSensorLED_Raises_TypeError_if_param_led_num_is_missing(self, kit):
        with pytest.raises(TypeError):
            kit.setSensorLED(led_setting=usp.GREEN)
    def test_setSensorLED_Raises_TypeError_if_param_led_setting_is_missing(self, kit):
        with pytest.raises(TypeError):
            kit.setSensorLED(led_num=0)
    def test_See_these_examples_for_setSensorLED(self, kit):
        lednum = 0
        assert kit.setSensorLED(usp.OFF, lednum).status == 'OK'
        assert kit.setSensorLED(usp.GREEN, lednum).status == 'OK'
        assert kit.setSensorLED(usp.RED, lednum).status == 'OK'
        lednum = 1
        assert kit.setSensorLED(usp.OFF, lednum).status == 'OK'
        assert kit.setSensorLED(usp.GREEN, lednum).status == 'OK'
        assert kit.setSensorLED(usp.RED, lednum).status == 'OK'
    def test_Restore_the_Sensor_LED_to_its_default_state(self, kit):
        kit.setSensorLED(usp.GREEN, 0)
        kit.setSensorLED(usp.GREEN, 1)

class TestCommandGetSensorConfig():
    def test_Call_getSensorConfig(self, kit):
        assert kit.getSensorConfig().status == 'OK'
    def test_getSensorConfig_Returns_str_BINNING_ON_or_str_BINNING_OFF(self, kit):
        binning = kit.getSensorConfig().binning
        assert binning == 'BINNING_ON' or binning == 'BINNING_OFF'
    def test_getSensorConfig_Returns_str_GAIN1X_or_str_GAIN2point5X_or_str_GAIN4X_or_str_GAIN5X(self, kit):
        gain = kit.getSensorConfig().gain
        assert (
            gain == 'GAIN1X' or
            gain == 'GAIN2_5X' or
            gain == 'GAIN4X' or
            gain == 'GAIN5X'
            )
    def test_getSensorConfig_Returns_str_ALL_ROWS_if_row_bitmap_is_0x1F(self, kit):
        row_bitmap = kit.getSensorConfig().row_bitmap
        assert row_bitmap == 'ALL_ROWS'
    def test_getSensorConfig_Returns_int_row_bitmap_if_row_bitmap_is_not_0x1F(self, kit):
        ROWS123 = 0x07
        kit.setSensorConfig(row_bitmap=ROWS123)
        row_bitmap = kit.getSensorConfig().row_bitmap
        assert row_bitmap == ROWS123

class TestCommandSetSensorConfig():
    def test_Call_setSensorConfig_using_default_params(self, kit):
        assert kit.setSensorConfig().status == 'OK'
    def test_setSensorConfig_default_params_are_BINNING_ON_GAIN1X_and_ALL_ROWS(self, kit):
        kit.setSensorConfig()
        assert kit.getSensorConfig().binning == 'BINNING_ON'
        assert kit.getSensorConfig().gain == 'GAIN1X'
        assert kit.getSensorConfig().row_bitmap == 'ALL_ROWS'
    def test_setSensorConfig_Returns_ERROR_if_param_binning_is_invalid(self, kit):
        assert kit.setSensorConfig(binning=2).status == 'ERROR'
    def test_setSensorConfig_Returns_ERROR_if_param_gain_is_invalid(self, kit):
        assert kit.setSensorConfig(gain=2).status == 'ERROR'
    def test_setSensorConfig_Returns_ERROR_if_param_row_bitmap_is_invalid(self, kit):
        # row_bitmap is invalid if three most-significant bits are set
        assert kit.setSensorConfig(row_bitmap=0xE0).status == 'ERROR'
        assert kit.setSensorConfig(row_bitmap=0xFF).status == 'ERROR'
    def test_setSensorConfig_Returns_OK_if_param_row_bitmap_is_0x00_ie_all_rows_off(self, kit):
        # Demonstrate it's OK to turn off all rows.
        assert kit.setSensorConfig(row_bitmap=0x00).status == 'OK'
        assert kit.getSensorConfig().row_bitmap == 0x00
    def test_See_this_example_for_setSensorConfig(self, kit):
        assert kit.setSensorConfig(
                usp.BINNING_OFF,
                usp.GAIN5X,
                row_bitmap=0x05
                ).status == 'OK'
    def test_Restore_the_default_pixel_configuration(self, kit):
        kit.setSensorConfig() # call with default values
        default_config = kit.getSensorConfig()
        assert default_config.binning == 'BINNING_ON'
        assert default_config.gain == 'GAIN1X'
        assert default_config.row_bitmap == 'ALL_ROWS'

class TestCommandGetExposure():
    def test_Call_getExposure(self, kit):
        assert kit.getExposure().status == 'OK'
    def test_getExposure_Returns_exposure_time_in_units_of_ms(self, kit):
        kit.setExposure(ms=5)
        assert kit.getExposure().ms == 5
    def test_getExposure_Returns_exposure_time_in_units_of_cycles(self, kit):
        kit.setExposure(cycles=250)
        assert kit.getExposure().cycles == 250

class TestCommandSetExposure():
    def test_Call_setExposure_specifying_exposure_time_in_units_of_ms(self, kit):
        assert kit.setExposure(ms=5).status == 'OK'
    def test_Call_setExposure_specifying_exposure_time_in_units_of_cycles(self, kit):
        assert kit.setExposure(cycles=5).status == 'OK'
    def test_setExposure_raises_TypeError_if_missing_a_time_param(self, kit):
        with pytest.raises(TypeError):
            kit.setExposure()
    def test_setExposure_raises_TypeError_if_there_is_more_than_one_time_param(self, kit):
        with pytest.raises(TypeError):
            kit.setExposure(ms=5, cycles=250)
    def test_See_these_examples_for_setExposure(self, kit):
        assert usp.to_ms(usp.MIN_CYCLES) == 0.02
        assert usp.to_ms(usp.MAX_CYCLES) == 1310.0
        assert kit.setExposure(ms=0.02).status == 'OK' # <--- min
        assert kit.setExposure(ms=0.10).status == 'OK'
        assert kit.setExposure(ms=1.00).status == 'OK'
        assert kit.setExposure(ms=10.0).status == 'OK'
        assert kit.setExposure(ms=100).status == 'OK'
        assert kit.setExposure(ms=1310).status == 'OK' # <--- max
    def test_Restore_the_exposure_time_to_the_default_value(self, kit):
        kit.setExposure(ms=1)

# class TestCommandCaptureFrame():
#     def test_Call_captureFrame(self, kit):
#         assert kit.captureFrame().status == 'OK'
