zstd --rm -d images/super.img.zst -o images/super.img
img2simg images/super.img images/super_new.img
fastboot flash dsp_ab images/dsp.img
fastboot flash xbl_config_ab images/xbl_config.img
fastboot flash boot_ab images/boot.img
fastboot flash modem_ab images/modem.img
fastboot flash vbmeta_system_ab images/vbmeta_system.img
fastboot flash tz_ab images/tz.img
fastboot flash vbmeta_ab images/vbmeta.img
fastboot flash bluetooth_ab images/bluetooth.img
fastboot flash abl_ab images/abl.img
fastboot flash cpucp_ab images/cpucp.img
fastboot flash dtbo_ab images/dtbo.img
fastboot flash featenabler_ab images/featenabler.img
fastboot flash vendor_boot_ab images/vendor_boot.img
fastboot flash keymaster_ab images/keymaster.img
fastboot flash uefisecapp_ab images/uefisecapp.img
fastboot flash qupfw_ab images/qupfw.img
fastboot flash xbl_ab images/xbl.img
fastboot flash devcfg_ab images/devcfg.img
fastboot flash hyp_ab images/hyp.img
fastboot flash imagefv_ab images/imagefv.img
fastboot flash shrm_ab images/shrm.img
fastboot flash aop_ab images/aop.img
fastboot flash super images/super_new.img
fastboot set_active a
fastboot erase userdata
fastboot erase metadata
fastboot reboot
