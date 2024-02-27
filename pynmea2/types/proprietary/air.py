# AIROHA

from ... import nmea


class AIR(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(AIR, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(AIR, self).__init__(manufacturer, data)

class AIR001(AIR):
    #    $PAIR001,002,0*39

    fields = (
        ("Packet_Type", "PAIR_No", int),
        ("PAIR_ACK", "ACK_No", int),
        ('Result', 'Exit_Code', int),
        # 0 = The command was successfully sent
        # 1 = The command is processing. You must wait for the result
        # 2 = Sending the command failed
        # 3 = This command ID is not supported
        # 4 = Command parameter error
        # 5 = MNL service is busy
    )


class AIR020(AIR):
    #    $PAIR020,AG3335M_V1.0.0.ER5_20200416,S,I,1003931,2003132012,a272,0,,,3aae182,2003132006,062ab13,2003132011,,*28

    fields = (
        ("Packet_Type", "PAIR_No", int),

        ('Project Version', 'SDK_Ver_Build_time'),
        # <Project_board>_<SDK version>_<SDK Build time>

        ('Frequency', 'Frequency'),
        # S: Single
        # D: Dual

        ('SW package', 'SW_package'),
        # N: Normal
        # W: Raw
        # T: Timing
        # R: RTK
        # I: NAVIC

        ('Service version', 'mnl_service'),
        ('Service build time', 'mnl_service_build_time'),

        ('DSP L1 rom version', 'L1_ROM_version'),
        ('DSP L1 ram version', 'L1_RAM_version'),

        ('DSP L5 rom version', 'L5_ROM_version'),
        ('DSP L5 ram version', 'L5_RAM_version'),

        ('Kernel version', 'mnl_kernel_version'),
        ('Kernel build time', 'mnl_kernel_build_time'),

        ('KF version', 'mnl_kf_version'),
        ('KF build time', 'mnl_kf_build_time'),

        ('RTK version', 'RTK_version'),
        ('RTK build time', 'RTK_build_time'),
    )

