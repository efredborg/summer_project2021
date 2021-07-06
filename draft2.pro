path_to_IRIS_l2 = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'


filename = 'iris2model_20140521_114758_3820258168_raster_t000_r00000.sav'
; restore, filename, /v

;raster_files = file_search(path_to_IRIS_l2+'/*iris_l2*raster*fits')  ; List of IRIS Level2 raster files
;iris2model = iris2(raster_files[10]) ; Default call: latest |IRIS2| database, considering all RPs (delta_mu=1), level=0, no weights
;iris2model = iris2(raster_files, version_db='v1.0', delta_mu=0.20, level=2)
iris2model = iris2(raster_files[11], weights=[1.,1/2.,1.,1/3.], level=1)


end
