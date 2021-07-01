goto,here
; DATA_DIR          = '/mn/stornext/d18/RoCS/kalogodu/data/'
; PROJECT           = 'iris_bp/'
; INSTRUMENT        = ['iris/','aia/','hmi/']
; DTYPE             = ['raster/','sji/']

; AIA_FILES         = FILE_SEARCH(DATA_DIR+PROJECT+INSTRUMENT[1]+'*.fits')
; HMI_FILES         = FILE_SEARCH(DATA_DIR+PROJECT+INSTRUMENT[2]+'*.fits')

; iris_data = data_dir+project+instrument[0]+dtype[0]
; f = IRIS_FILES(path = iris_data)
; fraster = IRIS_FILES('*raster*.fits',path = iris_data)
; fsji = IRIS_FILES('*SJI*.fits',path = iris_data)
; iris_read_l2,fraster,rindex,rdata

; calcheck=iris_prep_version_check(rindex, /loud)

; ****************************************************************************
; IRIS raster analysis
; ****************************************************************************
iris_data = '/mn/stornext/d10/HDC2/iris/data/level2_decompressed/2014/05/21/20140521_114758_3820258168/'

fraster = IRIS_FILES('*raster*.fits',path = iris_data)


d = iris_obj(fraster[0])
d->show_lines

;Spectral regions(windows)
; 0   1335.71   C II 1336    > A
; 1   1349.43   Fe XII 1349  > ..
; 2   1355.60   O I 1356     > ..
; 3   1393.78   Si IV 1394   > A
; 4   1402.77   Si IV 1403   > A
; 5   2832.75   2832         > ..
; 6   2814.47   2814         > ..
; 7   2796.20   Mg II k 2796 > A
; READ_IRIS_L2,fraster,rindex,rdata
; rdata_clean = IRIS_DUSTBUSTER(rindex,rdata,clean_values,/run)
read_iris_l2,fraster,rindex,rdata,wave='Si IV 1403'

obs_time       = rindex.date_obs
exp_time       = rindex.exptime
xcen           = rindex[0].xcen
ycen           = rindex[0].ycen
fovx           = rindex[0].fovx
fovy           = rindex[0].fovy
line           = rindex[0].wavename
cen_wavelength = rindex[0].wavelnth
wavelnth       = d->getlam('Si IV 1403')
; print,'obs_time       =',obs_time
; print,'exp_time       =',exp_time
print,'xcen           =',xcen
print,'ycen           =',ycen
print,'fovx           =',fovx
print,'fovy           =',fovy
print,'line           =',line
print,'cen_wavelength =',cen_wavelength
print,'Wavelenght     =',minmax(wavelnth)
DATA_DIR='/mn/stornext/d18/RoCS/kalogodu/data/iris_bp/iris/raster/siiv1403/'
save, rdata,rindex,obs_time,exp_time,xcen,ycen,fovx,fovy,line,cen_wavelength,wavelnth,filename= DATA_DIR+'iris_raster_1403.sav',description='Si IV 1403 4 step rasters (660) data'
here:
DATA_DIR='/mn/stornext/d18/RoCS/kalogodu/data/iris_bp/iris/raster/siiv1403/'
filename = DATA_DIR+'iris_raster_1403.sav'
restore,filename,/v
a    = 130
b    = 192
lam  = wavelnth[a:b]
data = rdata[a:b,*,*,*]
;reference wavelength calculation
lp = average(data>0.,[2,3,4])
yfit_avg = gaussfit(lam,lp,coeff,nterms=5)
ref_wavelength = coeff[1]
; print,ref_wavelength
; window,1
; plot,lam,lp,/xs,/ys
; oplot,lam,yfit,color=cgcolor('green')
; stop

c = 2.997924580d5     ; km/s
sz   = size(data,/dimensions)
intensity = fltarr(sz[1],sz[2],sz[3])
width     = fltarr(sz[1],sz[2],sz[3])
velocity  = fltarr(sz[1],sz[2],sz[3])

for i = 0, sz[1]-1 do begin
	for j = 0, sz[2]-1 do begin
		for k = 0, sz[3]-1 do begin
			lp   = reform(data[*,i,j,k]>0.)
			yfit = gaussfit(lam,lp,coeff,NTERMS=5)

			fwhm = 2.*sqrt(2*alog(2))*coeff[2]
			int  = sqrt(2.*!pi)*coeff[0]*coeff[2]
			vell =  ((coeff[1]-ref_wavelength)/ref_wavelength)*c

			intensity[i,j,k] = int
			width[i,j,k]     = fwhm
			velocity[i,j,k]  = vell
		endfor
	endfor
endfor

save,intensity,width,velocity,filename= DATA_DIR+'iris_raster_1403_sgfit.sav',description='Sigle gaussfit for the Si IV 1403 raster data, reference wavelength is taken as central wavelength position of sigle gaussfit to the average profile. average profile is average over all y pixels, steps, and rasters.'
; lp = average(data>0.,[2,3,4])
; yfit_avg = gaussfit(lam,lp,coeff,nterms=5)
; filename = DATA_DIR+'iris_raster_1403_sgfit.sav'
; restore,filename,/v
img = reform(velocity[*,0,*])
img = transpose(img)
eis_colors,/vel
wset,1
plot_image,img>(-20.)<20.
cursor,x,y
print,x,y
lp = reform(rdata[130:192,y,0,x])>0.
window,0
loadct,0
plot,lam,lp,/xs,/ys
yfit = gaussfit(lam,lp,coeff,nterms=5)
vell =  ((coeff[1]-ref_wavelength)/ref_wavelength)*c
oplot,lam,yfit,color=cgcolor('green')
oplot,lam,yfit_avg,color=cgcolor('red'),linestyle=2
print,vell

k_clusters = 5
data_sel = reform(data[*,300:500,0,*])
help,data_sel
sz = size(data_sel,/dimensions)

ress = fltarr(sz[1],sz[2])
help,res
for i = 0, sz[1]-1 do begin
		dats = reform(data_sel[*,i,*])
		wc = clust_wts(dats,n_clusters=k_clusters,n_iterations=50,/doub)
		res=cluster(dats,wc,n_c=k_clusters)
		; res[i,*] = reform(res[0,*])
		ress[i,*] = res
endfor

clu = 3
p = data_sel(where(ress eq clu))
img = ress*0
img(p)=1
rrimg= data_sel
help,ress
sz = size(data_sel,/dimensions)
for i = 0, sz[0]-1 do begin
	rimg = reform(data_sel[i,*,*])*img
	rrimg[i,*,*]=rimg
endfor

lp = average(rrimg,[2,3])
window,3
plot,lam,lp,/xs,/ys,title=clu
loadct,0
end
