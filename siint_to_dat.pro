filename = 'siint_400.sav'
restore, filename

length = uint(size(siint400, /dimensions))
length = length[0]
print, length

openw, 1, 'siint_400.dat'
for i=0, length -1 do begin
  printf, 1, siint400[i]
  endfor
close, 1
end
