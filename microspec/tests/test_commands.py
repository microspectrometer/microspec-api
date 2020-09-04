import microspec as usp
import pytest
import warnings

def restore_Bridge_LED(kit, verbose=False):
    kit.setBridgeLED(usp.GREEN)
    if verbose: print("Restored Bridge LED to default state.")

def restore_Sensor_LEDs(kit, verbose=False):
    kit.setSensorLED(usp.GREEN, 0)
    kit.setSensorLED(usp.GREEN, 1)
    if verbose: print("Restored Sensor LEDs to default state.")

def restore_pixel_configuration(kit, verbose=False):
    kit.setSensorConfig() # call with default values
    default_config = kit.getSensorConfig()
    assert default_config.binning == 'BINNING_ON'
    assert default_config.gain == 'GAIN1X'
    assert default_config.row_bitmap == 'ALL_ROWS'
    if verbose: print("Restored pixel configuration to default state.")

def restore_exposure_time(kit, verbose=False):
    kit.setExposure(ms=1)
    if verbose: print("Restored exposure time to default state.")

@pytest.fixture(scope="class")
def restore_defaults(kit): # test setup run once per class
    """Restore dev-kit to its default state before each test class.

    See test setup print statements on stdout
    -----------------------------------------
    Do both of the following:

    - set ``verbose=True`` in the body of ``restore_defaults``
    - run pytest with option ``-s``

    Parameter kit
    -------------
    Parameter ``kit`` is an instance of Devkit with session
    scope. It comes from the test fixture in ``conftest.py``.

    Why class scope?
    ----------------
    Setting default values takes up some time because it involves
    hardware I/O. Rather than restore default values before
    **every test**, the scope is set to "class" to restore
    defaults **only at the start of each test group**.

    How to run setup code once PER CLASS
    ------------------------------------
    Tests are grouped by command name into test classes. Each
    test class inherits from the ``Setup`` class. (``Setup`` is
    **not** a special class name recognized by ``pytest``.)

    .. code-block:: python

        class Setup():
            def test_Restore_defaults(self, restore_defaults): pass

    The ``Setup`` class has only one test. This test does not
    test anything. It is named with the ``test_`` prefix
    so that ``pytest`` runs it. This test uses the
    ``restore_defaults`` test fixture. A simplified version of
    the fixture looks like this:

    .. code-block:: python

        @pytest.fixture(scope="class")
        def restore_defaults(kit):
            do_setup()
            print("Setup done.")
            yield

    The following explains:

    - how scope works for "class"
    - how a class uses the fixture
    - why there is a yield statement

    Scope "class"
    -------------

    The test fixture runs once per class because it has "class"
    scope.

    Which classes use the test fixture
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Classes only run this test fixture if they have a test (a
    method) that uses this fixture. It does not matter how many
    of the tests use the fixture, the setup code in the fixture
    still only runs once at the beginning of the class's tests.
    But at least one test must use the fixture.

    How does a class use the test fixture
    -------------------------------------
    The class needs a test (a method with the prefix ``test_``
    that uses the fixture. To use the fixture, the test only has
    to include the fixture name in its argument list. The test
    body is just a ``pass`` statement:

    .. code-block:: python

        def test_Restore_defaults(self, restore_defaults): pass

    Instead of copying the above code into every class, the code
    is placed in class ``Setup`` and the test classes inherits
    from class ``Setup``. The run-time effect is exactly the
    same: every class has one test that uses the fixture, so the
    fixture code runs once per class.

    Yield
    -----
    The test fixture has a ``yield`` statement, but yields
    nothing. The ``yield`` statement serves as a separator
    between **setup** code and **teardown** code. Any code before
    the ``yield`` statement is setup. Any code after the
    ``yield`` statement is teardown.
    """
    verbose = True
    if verbose: print("\nTest setup:")
    restore_Bridge_LED(kit, verbose)
    restore_Sensor_LEDs(kit, verbose)
    restore_pixel_configuration(kit, verbose)
    restore_exposure_time(kit, verbose)
    yield

class Setup():
    def test_Restore_defaults(self, restore_defaults): pass

@pytest.fixture
def restore_timeout(kit):
    """Restore kit timeout to its default after each test.

    Tests must include ``restore_timeout`` in their argument list
    to restore the timeout:

    .. code-block:: python

        def test_captureFrame_Automatically_increases_timeout_if_it_is_less_than_exposure_time(
            self,
            kit,
            restore_timeout # <--- sets timeout to 2s after test runs
            ):
            ...
    """
    yield
    kit.timeout = 2.0

class TestCommandGetBridgeLED(Setup):
    def test_getBridgeLED_Returns_status_OK_after_power_on(self, kit):
        assert kit.getBridgeLED().status == 'OK'
    def test_getBridgeLED_Returns_led_setting_GREEN_after_power_on(self, kit):
        assert kit.getBridgeLED().led_setting == 'GREEN'
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

class TestCommandSetBridgeLED(Setup):
    def test_setBridgeLED_Returns_status_OK_after_power_on(self, kit):
        assert kit.setBridgeLED(usp.GREEN).status == 'OK'
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

class TestCommandGetSensorLED(Setup):
    def test_getSensorLED_Returns_status_OK_after_power_on(self, kit):
        assert kit.getSensorLED(0).status == 'OK'
    def test_getSensorLED_0_Returns_led_setting_OFF_after_power_on(self, kit):
        assert kit.getSensorLED(0).led_setting == 'OFF'
    def test_getSensorLED_1_Returns_led_setting_GREEN_after_power_on(self, kit):
        assert kit.getSensorLED(1).led_setting == 'GREEN'
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

class TestCommandSetSensorLED(Setup):
    def test_Restore_defaults(self, restore_defaults): pass
    def test_setSensorLED_Returns_status_OK_after_power_on(self, kit):
        assert kit.setSensorLED(usp.GREEN, 0).status == 'OK'
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

class TestCommandGetSensorConfig(Setup):
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

class TestCommandSetSensorConfig(Setup):
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

class TestCommandGetExposure(Setup):
    def test_Devkit_is_instantiated_with_default_exposure_time(self, kit):
        default_exposure_ms = 1.0
        default_exposure_cycles = usp.to_cycles(default_exposure_ms)
        assert kit.exposure_time_cycles == default_exposure_cycles
        assert kit.exposure_time_ms     == default_exposure_ms
    def test_getExposure_Updates_Devkit_exposure_time_attrs(self, kit):
        kit.setExposure(ms=2.0)
        exposure_time = kit.getExposure()
        assert kit.exposure_time_cycles == exposure_time.cycles
        assert kit.exposure_time_ms     == exposure_time.ms
    def test_Call_getExposure(self, kit):
        assert kit.getExposure().status == 'OK'
    def test_getExposure_Returns_exposure_time_in_units_of_ms(self, kit):
        kit.setExposure(ms=5)
        assert kit.getExposure().ms == 5
    def test_getExposure_Returns_exposure_time_in_units_of_cycles(self, kit):
        kit.setExposure(cycles=250)
        assert kit.getExposure().cycles == 250

class TestCommandSetExposure(Setup):
    def test_setExposure_Updates_Devkit_exposure_time_attrs(self, kit):
        new_time_ms = 2.0
        kit.setExposure(ms=new_time_ms)
        assert kit.exposure_time_cycles == usp.to_cycles(new_time_ms)
        assert kit.exposure_time_ms     == new_time_ms

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

class TestCommandCaptureFrame(Setup):
    def test_Call_captureFrame(self, kit):
        reply = kit.captureFrame()
        assert reply.status == 'OK'
        assert reply.num_pixels == 392
        assert len(reply.pixels) == reply.num_pixels
    def test_captureFrame_Automatically_increases_timeout_if_it_is_less_than_exposure_time(
            self, kit, restore_timeout
            ):
        kit.setExposure(ms=20)
        kit.timeout = .01 # 10 milliseconds
        reply = kit.captureFrame()
        assert reply.status == 'OK'
        assert reply.num_pixels == 392
        assert len(reply.pixels) == reply.num_pixels
        assert type(reply.pixels) == list
        assert len(reply.frame) == reply.num_pixels
        assert type(reply.frame) == dict
    def test_captureFrame_Issues_timeout_warning_if_command_timeouts(
            self, kit, monkeypatch
            ):
        with monkeypatch.context() as m:
            m.setattr(kit, "_is_out_of_time", lambda reply : "True")
            with pytest.warns(UserWarning, match="Command captureFrame timed out."):
                kit.captureFrame()
    def test_captureFrame_Returns_status_TIMEOUT_if_command_timeouts(
            self, kit, monkeypatch
            ):
        with monkeypatch.context() as m:
            m.setattr(kit, "_is_out_of_time", lambda reply : "True")
            with pytest.warns(UserWarning):
                assert kit.captureFrame().status == 'TIMEOUT'
    def test_captureFrame_Returns_num_pixels_is_0_if_command_timeouts(
            self, kit, monkeypatch
            ):
        with monkeypatch.context() as m:
            m.setattr(kit, "_is_out_of_time", lambda reply : "True")
            with pytest.warns(UserWarning):
                assert kit.captureFrame().num_pixels == 0
    def test_captureFrame_Returns_empty_list_for_pixels_if_command_timeouts(
            self, kit, monkeypatch
            ):
        with monkeypatch.context() as m:
            m.setattr(kit, "_is_out_of_time", lambda reply : "True")
            with pytest.warns(UserWarning):
                assert kit.captureFrame().pixels == []
    def test_captureFrame_Returns_empty_dict_for_frame_if_command_timeouts(
            self, kit, monkeypatch
            ):
        with monkeypatch.context() as m:
            m.setattr(kit, "_is_out_of_time", lambda reply : "True")
            with pytest.warns(UserWarning):
                assert kit.captureFrame().frame == {}
    def test_Call_captureFrame_again_to_see_monkeypatch_is_gone(self, kit):
        reply = kit.captureFrame()
        assert reply.status == 'OK'
        assert reply.num_pixels == 392
        assert len(reply.pixels) == reply.num_pixels
