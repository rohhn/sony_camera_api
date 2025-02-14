exist_param = ["setShootMode",
               "startLiveviewWithSize",
               "setLiveviewFrameInfo",
               "actZoom",
               "setZoomSetting",
               "setLiveviewSize", # Not listed in API 2.20?
               "setTouchAFPosition",
               "actTrackingFocus",
               "setTrackingFocus",
               "setContShootingMode",
               "setContShootingSpeed",
               "setSelfTimer",
               "setExposureMode",
               "setFocusMode",
               "setExposureCompensation",
               "setFNumber",
               "setShutterSpeed",
               "setIsoSpeedRate",
               "setWhiteBalance",
               "setProgramShift",
               "setFlashMode",
               "setBeepMode",
               "setStillSize",
               "setStillQuality",
               "setPostviewImageSize",
               "setMovieFileFormat",
               "setMovieQuality",
               "setSteadyMode",
               "setViewAngle",
               "setSceneSelection",
               "setColorSetting",
               "setIntervalTime",
               "setLoopRecTime",
               "setFlipSetting",
               "setTvColorSystem",
               "getWindNoiseReduction",
               "getSupportedWindNoiseReduction",
               "getAvailableWindNoiseReduction",
               "setCameraFunction",
               "setAudioRecording",
               "setWindNoiseReduction",
               "getSourceList",
               "getContentCount",
               "getContentList",
               "setStreamingContent",
               "seekStreamingPosition",
               "requestToNotifyStreamingStatus",
               "deleteContent",
               "setInfraredRemoteControl",
               "setAutoPowerOff",
               "setBeepMode",
               "setCurrentTime",
               "getSourceList",
               "getContentCount",
               "getContentList",
               "setStreamingContent",
               "seekStreamingPosition",
               "requestToNotifyStreamingStatus",
               "deleteContent",
               "getEvent", # version 1.0, 1.1, 1.2
               "getMethodTypes"]
no_param = ["getShootMode",
            "getSupportedShootMode",
            "getAvailableShootMode",
            "actTakePicture",
            "actHalfPressShutter",
            "cancelHalfPressShutter",
            "awaitTakePicture",
            "startContShooting",
            "stopContShooting",
            "startMovieRec",
            "stopMovieRec",
            "startLoopRec",
            "stopLoopRec",
            "startAudioRec",
            "stopAudioRec",
            "startIntervalStillRec",
            "stopIntervalStillRec",
            "startLiveview",
            "stopLiveview",
            "getLiveviewSize",
            "getSupportedLiveviewSize",
            "getAvailableLiveviewSize",
            "getLiveviewFrameInfo",
            "getZoomSetting",
            "getSupportedZoomSetting",
            "getAvailableZoomSetting",
            "actHalfPressShutter",
            "cancelHalfPressShutter",
            "getTouchAFPosition",
            "cancelTouchAFPosition",
            "cancelTrackingFocus",
            "getTrackingFocus",
            "getSupportedTrackingFocus",
            "getAvailableTrackingFocus",
            "getContShootingMode",
            "getSupportedContShootingMode",
            "getAvailableContShootingMode",
            "getContShootingSpeed",
            "getSupportedContShootingSpeed",
            "getAvailableContShootingSpeed",
            "getSelfTimer",
            "getSupportedSelfTimer",
            "getAvailableSelfTimer",
            "getExposureMode",
            "getSupportedExposureMode",
            "getAvailableExposureMode",
            "getFocusMode",
            "getSupportedFocusMode",
            "getAvailableFocusMode",
            "getExposureCompensation",
            "getSupportedExposureCompensation",
            "getAvailableExposureCompensation",
            "getFNumber",
            "getSupportedFNumber",
            "getAvailableFNumber",
            "getShutterSpeed",
            "getSupportedShutterSpeed",
            "getAvailableShutterSpeed",
            "getIsoSpeedRate",
            "getSupportedIsoSpeedRate",
            "getAvailableIsoSpeedRate",
            "getWhiteBalance",
            "getSupportedWhiteBalance",
            "getAvailableWhiteBalance",
            "actWhiteBalanceOnePushCustom",
            "getSupportedProgramShift",
            "getFlashMode",
            "getSupportedFlashMode",
            "getAvailableFlashMode",
            "getStillSize",
            "getSupportedStillSize",
            "getAvailableStillSize",
            "getStillQuality",
            "getSupportedStillQuality",
            "getAvailableStillQuality",
            "getPostviewImageSize",
            "getSupportedPostviewImageSize",
            "getAvailablePostviewImageSize",
            "getMovieFileFormat",
            "getSupportedMovieFileFormat",
            "getAvailableMovieFileFormat",
            "getMovieQuality",
            "getSupportedMovieQuality",
            "getAvailableMovieQuality",
            "getSteadyMode",
            "getSupportedSteadyMode",
            "getAvailableSteadyMode",
            "getViewAngle",
            "getSupportedViewAngle",
            "getAvailableViewAngle",
            "getSceneSelection",
            "getSupportedSceneSelection",
            "getAvailableSceneSelection",
            "getColorSetting",
            "getSupportedColorSetting",
            "getAvailableColorSetting",
            "getIntervalTime",
            "getSupportedIntervalTime",
            "getAvailableIntervalTime",
            "getLoopRecTime",
            "getSupportedLoopRecTime",
            "getAvailableLoopRecTime",
            "getFlipSetting",
            "getSupportedFlipSetting",
            "getAvailableFlipSetting",
            "getTvColorSystem",
            "getSupportedTvColorSystem",
            "getAvailableTvColorSystem",
            "startRecMode",
            "stopRecMode",
            "getCameraFunction",
            "getSupportedCameraFunction",
            "getAvailableCameraFunction",
            "getAudioRecording",
            "getSupportedAudioRecording",
            "getAvailableAudioRecording",
            "getSchemeList",
            "startStreaming",
            "pauseStreaming",
            "stopStreaming",
            "getInfraredRemoteControl",
            "getSupportedInfraredRemoteControl",
            "getAvailableInfraredRemoteControl",
            "getAutoPowerOff",
            "getSupportedAutoPowerOff",
            "getAvailableAutoPowerOff",
            "getBeepMode",
            "getSupportedBeepMode",
            "getAvailableBeepMode",
            "getSchemeList",
            "getStorageInformation",
            "actFormatStorage", # found in firmware reversing
            "getAvailableApiList",
            "getApplicationInfo",
            "getVersions",
            "getMethodTypes",
            "startBulbShooting",
            "stopBulbShooting"] #  camera, system and avContent

params = [{"name":"shoot mode",
           "value": ["still", "movie", "audio", "intervalstill"],
           "message": """
           "still"              Still image shoot mode
           "movie"              Movie shoot mode
           "audio"              Audio shoot mode
           "intervalstill"      Interval still shoot mode
           """},
          {"name":"liveview size",
           "value": ["L", "M"],
           "message": """
           "L"           XGA size scale (the size varies depending on
                         the camera models, and some camera models change
                         the liveview quality instead of making the size larger.)
           "M"           VGA size scale (the size varies depending on the camera models)
           """},
           # [TODO] add more ...
          ]
