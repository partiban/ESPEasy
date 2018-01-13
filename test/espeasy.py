### High level ESPEasy config.
### Things like configging a controller or device via http
### I've created it in way that you can just copy/past form parameters from Chromium's header view


class EspEasy:

    def __init__(self, node):
        self._node=node


    def control(self, **kwargs):
        self._node.log.info("Control "+str(kwargs))
        self._node.http_post(
            page="control",

            params="""
                cmd:{cmd}
            """.format(**kwargs),

        )


    def controller_domoticz_mqtt(self, **kwargs):
        """config controller to use domoticz via mqtt"""

        self._node.log.info("Config controller domoticz mqtt "+str(kwargs))
        self._node.http_post(
            twice=True, # needed for controllers and devices because of the way its implemented
            page="controllers",

            params="""
                index:{index}
            """.format(**kwargs),

            data="""
                protocol:2
                usedns:0
                controllerip:{controllerip}
                controllerport:1883
                controlleruser:
                controllerpassword:
                controllersubscribe:domoticz/out
                controllerpublish:domoticz/in
                controllerenabled:on
            """.format(**kwargs)
        )


    def controller_domoticz_http(self, **kwargs):
        """config controller to use domoticz via http"""

        self._node.log.info("Config controller domoticz http "+str(kwargs))
        self._node.http_post(
            twice=True, # needed for controllers and devices because of the way its implemented
            page="controllers",

            params="""
                index:{index}
            """.format(**kwargs),

            data="""
                protocol:1
                usedns:0
                controllerip:{controllerip}
                controllerport:{controllerport}
                controlleruser:
                controllerpassword:
                controllerenabled:on
            """.format(**kwargs)
        )

    def device_p001(self, **kwargs):
        self._node.log.info("Config device plugin p001 "+str(kwargs))

        self._node.http_post(
            twice=True, # needed for controllers and devices because of the way its implemented
            page="devices",

            params="""
                index:{index}
            """.format(**kwargs),

            data="""
                TDNUM:1
                TDN:
                TDE:on
                taskdevicepin1:{taskdevicepin1}
                plugin_001_type:{plugin_001_type}
                plugin_001_button:{plugin_001_button}
                TDSD1:on
                TDID1:{TDID1}
                TDT:0
                TDVN1:Switch
                edit:1
            """.format(**kwargs)
        )


    def device_p004(self, **kwargs):
        self._node.log.info("Config device plugin p004 "+str(kwargs))

        self._node.http_post(
            twice=True, # needed for controllers and devices because of the way its implemented
            page="devices",

            params="""
                index:{index}
            """.format(**kwargs),

            data="""
                TDNUM:4
                TDN:temp
                TDE:on
                taskdevicepin1:{taskdevicepin1}
                plugin_004_dev:{plugin_004_dev}
                plugin_004_res:{plugin_004_res}
                TDT:5
                TDVN1:Temperature
                TDF1:
                TDVD1:2
                TDSD1:on
                TDID1:{TDID1}
                edit:1
                page:1
            """.format(**kwargs)
        )

    def device_p036(self, **kwargs):
        self._node.log.info("Config device plugin p036 "+str(kwargs))

        self._node.http_post(
            twice=True, # needed for controllers and devices because of the way its implemented
            page="devices",

            params="""
                index:{index}
            """.format(**kwargs),

            data="""
                TDNUM:36
                TDN:
                TDE:on
                plugin_036_adr:60
                plugin_036_rotate:1
                plugin_036_nlines:1
                plugin_036_scroll:1
                Plugin_036_template1:espeasy
                Plugin_036_template2:test
                Plugin_036_template3:suite
                Plugin_036_template4:test1
                Plugin_036_template5:test2
                Plugin_036_template6:test3
                Plugin_036_template7:test4
                Plugin_036_template8:test5
                Plugin_036_template9:test6
                Plugin_036_template10:test7
                Plugin_036_template11:test8
                Plugin_036_template12:test9
                taskdevicepin3:-1
                plugin_036_timer:0
                TDT:1
                edit:1
                page:1
            """.format(**kwargs)
        )
