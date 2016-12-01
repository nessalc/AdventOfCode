f=File.open("C:\\Users\\James\\Documents\\programming\\advent2016\\input01.txt")
directions=f.read
compass='NESW'
x,y,f=0,0,'N'
locations=[]
directions.split(', ').each do |d|
  lr,dist=d[/[LR]/],d[/\d+/].to_i
  if lr=='L' then
    f=compass[(compass.index(f)-1)%4]
  else
    f=compass[(compass.index(f)+1)%4]
  end
  if f=='N' then
    y+=dist
  elsif f=='E' then
    x+=dist
  elsif f=='S' then
    y-=dist
  elsif f=='W' then
    x-=dist
  end
  locations+=[[x,y]]
end
puts x.to_s+'+'+y.to_s+'='+(x+y).to_s