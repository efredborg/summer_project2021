pro load_files
  data_dir = '/mn/stornext/d9/iris/data/level2/2014/05/21/20140521_114758_3820258168'
  files = find_files('iris_l2*raster*fits', data_dir+'*/')
  dim_files = size(files)
  for j = 0, dim_files[1]-1 do print, j,' - ',  strmid(files[j], strpos(files[j],'iris_l2'),100)
  end

pro inversion
  data_iris = get_info_irisl2(files[10], factor_and_data=1, mgii_only=1)
  help, data_iris


2014-05-21T11:54:10.940 # raster=10
2014-05-21T12:49:59.910 # raster=100
