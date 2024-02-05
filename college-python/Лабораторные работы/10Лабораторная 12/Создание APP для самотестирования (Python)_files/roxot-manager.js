(function (c) {
    if (isEngineInited()){
        return;
    }

    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.async = 1;
    script.src = c.managerUrl;
    script.dataset.roxotInited = 'true';

    let head = document.getElementsByTagName('head')[0];
    head.insertBefore(script, head.firstChild);

    window.rom = window.rom || {cmd: [], icmd: []};
    window.rom.icmd = window.rom.icmd || [];
    window.rom.icmd.push(c);

    function isEngineInited(){
        return  document.querySelectorAll('[data-roxot-inited]').length;
    }
})({"publisherId":"c427193e-c45c-4b31-b9de-0d5bc41115fd","publisher":"TechMedia","adBlockMode":"iframe","iframeSspList":["google","prebid","prebid_dfp"],"managerUrl":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/common-engine.js?v=s-ff183091-151b-47af-9790-8a477e06f4e1","wrapperUrl":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/wrapper.js?v=s-ff183091-151b-47af-9790-8a477e06f4e1","placementConfigTemplate":"https:\/\/cdn.skcrtxr.com\/wrapper-builder\/placement\/__PLACEMENT_ID__?v=d-1667380856","gfsPlacementOptionsTemplate":"https:\/\/cdn.skcrtxr.com\/wrapper-builder\/gfs-placement\/__PLACEMENT_ID__?v=d-1667380856","isLanguageSpecific":true,"hostConfig":{"habr.com":{"wrapperOptions":[],"isAcceptableAdsEnabled":false}},"isBrowserSpecific":false,"isOsSpecific":false,"isDeviceTypeSpecific":false,"isGeoSpecific":false,"isGetParamSpecific":false,"dynamicUrlTemplate":"","wrapperConfig":{"monetizationStatsIntegration":{"enabled":true,"requestSettings":{"isNeedToSend":true,"sampleCoefficient":1},"impressionSettings":{"isNeedToSend":true,"sampleCoefficient":1}},"host":"habr.com","engineFileName":"common-engine.js","enableAdFirstLoadInHiddenTab":true,"universalPlaceHolder":{"enabled":false},"prebid":{"prebidTimeout":1500,"adjustment":{"adriver":1,"appnexus":0.95,"between":1,"criteo":0.9,"getintent":0.06,"mytarget":0.1,"otm":0.96,"rtbhouse":1,"rubicon":0.98},"path":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/prebid.js?v=s-ff183091-151b-47af-9790-8a477e06f4e1"},"adfox":{"hb":{"biddersMap":{"betweenDigital":"1945468","myTarget":"1945461","otm":"1945469","segmento":"1945470","getintent":"1945477","hybrid":"1945478","adriver":"1945479","buzzoola":"1945480","relap":"1945481","adfox_yandex_premium-publisher-network":"1946302","mts":"2030417","mediasniper":"2032962","adfox_yandex_roxot-adfox-hb":"2043702","rtbhouse":"1393902","criteo":"1393905","videonow":"1407059"},"timeout":1000}},"roxotYaMetric":{"enabled":true,"counterId":88477929},"videojsLibs":{"path":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/video-libs.js?v=s-ff183091-151b-47af-9790-8a477e06f4e1"},"pageUrlVariableName":"roxotPlusPageUrl","stubVideoPath":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/video-ad?v=s-ff183091-151b-47af-9790-8a477e06f4e1","adfoxIntegrationType":"direct","yandexIntegrationType":"common"},"lazyLoading":[],"geoSpecificUrl":"https:\/\/geo-worker.skcrtxr.com\/api\/geo\/region"})