f=File.open(ARGV[0])
lines=f.readlines()
re=/((?:\w*-)+)(\d+)\[(\w{5})\]/
idsum=0
lines.each do |room|
  roomname=room[re,1]
  temp=roomname.gsub(/-/,'').chars
  hashmap=Hash.new(0)
  temp.each { |t| hashmap[t]+=1 }
  r=[]
  hashmap.values.sort.reverse[0,5].each do |v|
    tr=[]
    while hashmap.has_value?(v)
      key=hashmap.rassoc(v)[0]
      tr+=[key]
      hashmap.delete(key)
    end
    tr.sort!
    r+=tr
  end
  r=r.join()[0,5]
  if r==room[re,3]
    sectorid=room[re,2].to_i
    idsum+=sectorid
    (0...sectorid).each do
      roomname.tr!('abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza')
    end
    if roomname.include?('northpole')
      puts "#{roomname.gsub(/-/,' ')}, sector #{sectorid}"
    end
  end
end
puts "Part 1: Sector ID Sum of real rooms is #{idsum}"
