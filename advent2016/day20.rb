f=File.open(ARGV[0])
lines=f.readlines()
def combine_ranges(range1,range2)
  if range2===range1.begin and range2===range1.end
    return range2
  elsif range1===range2.begin and range1===range2.end
    return range1
  elsif range2===range1.begin
    return range2.begin..range1.end
  elsif range1===range2.begin
    return range1.begin..range2.end
  elsif range2.begin==range1.end+1
    return range1.begin..range2.end
  elsif range1.begin==range2.end+1
    return range2.begin..range1.end
  elsif range1.begin>range2.end or range2.begin>range1.end
    return nil
  end
end
def add_range(range_array,range)
  range_array.each_index do |i|
    t=range_array[i]
    combined=combine_ranges(t,range)
    if combined
      range_array[i]=combined
      break
    elsif i<range_array.length-1
      next
    else
      range_array<<range
    end
  end
  return range_array
end
def range_array_size(range)
  return range.reduce(0){|size,nr|size+(nr.end-nr.begin+1)}
end
blacklist=[]
line=lines.shift
a,b=line.strip.split('-').map{|t|t.to_i}
blacklist<<(a..b)
lines.each do |line|
  a,b=line.strip.split('-').map{|t|t.to_i}
  range=a..b
  add_range(blacklist,range)
end
blacklist.sort_by!{|range|range.begin}
begin
  temp=[blacklist[0]]
  prev_len=blacklist.length
  (1...blacklist.length).each do |bli|
    add_range(temp,blacklist[bli])
  end
  len=temp.length
  if len!=prev_len then blacklist=temp end
end while len!=prev_len
puts "Part 1: Lowest Valid IP is #{blacklist[0].end+1}"
puts "Part 2: #{2**32-range_array_size(blacklist)} IPs available"
