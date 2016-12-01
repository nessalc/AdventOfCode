f=File.open(ARGV[0])
directions=f.read
compass='NESW'
x,y,f=0,0,'N'
locations=[[x,y]]
directions.split(', ').each do |d|
  lr,dist=d[/[LR]/],d[/\d+/].to_i
  if lr=='L' then
    f=compass[(compass.index(f)-1)%4]
  else
    f=compass[(compass.index(f)+1)%4]
  end
  xp,yp=x,y
  temp=[]
  if f=='N' then
    y+=dist
    ((yp+1)..y).each do |j|
      temp+=[[x,j]]
    end
  elsif f=='E' then
    x+=dist
    ((xp+1)..x).each do |i|
      temp+=[[i,y]]
    end
  elsif f=='S' then
    y-=dist
    (y...yp).each do |j|
      temp+=[[x,j]]
    end
    temp.reverse!
  elsif f=='W' then
    x-=dist
    (x...xp).each do |i|
      temp+=[[i,y]]
    end
    temp.reverse!
  end
  locations+=temp
end
puts "part 1: #{x.abs}+#{y.abs}=#{x.abs+y.abs}"
duplicate_found=false
for i in 1...locations.length
  if !duplicate_found
    index=locations[0,i].index(locations[i])
    if index
      x,y=locations[i]
      duplicate_found=true
    end
  end
end
puts "part 2: #{x.abs}+#{y.abs}=#{x.abs+y.abs}"
