f=File.open(ARGV[0])
lines=f.readlines()
count=0
lines.partition.each do |line|
  #supernet sequences *outside* brackets
  #hypernet sequences *inside* brackets
  hypernet=line.scan(/(?<=\[)\w*/)
  supernet=line.scan(/\w*(?=\[)|(?<=\])\w*/)
  #supports TLS
    #contains abba *outside* square brackets
  abba=false
  hypernet.each do |test|
    t=test.match(/(\w)(\w)\2\1/)
    if t
      abba|=(t[1]!=t[2])
    end
  end
  if abba
    next
  end
  supernet.each do |test|
    t=test.match(/(\w)(\w)\2\1/)
    if t
      abba|=(t[1]!=t[2])
    end
  end
  if abba
    count+=1
  end
end
lines.partition.each do |line|
  #supernet sequences *outside* brackets
  #hypernet sequences *inside* brackets
  hypernet=line.scan(/(?<=\[)\w*/)
  supernet=line.scan(/\w*(?=\[)|(?<=\])\w*/)
  #supports SSL
    #contains aba *outside* square brackets
    #contains bab *inside* square brackets
  aba=false
end
puts "Part 1: #{count} Addresses support TLS"
