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
puts "Part 1: #{count} Addresses support TLS"
count=0
lines.partition.each do |line|
  #supernet sequences *outside* brackets
  #hypernet sequences *inside* brackets
  hypernet=line.scan(/(?<=\[)\w+/)
  supernet=line.scan(/\w+(?=\[)|(?<=\])\w+/)
  #supports SSL
    #contains aba *outside* square brackets
    #contains bab *inside* square brackets
  ssl=false
  supernet.each do |segment|
    pos=segment.index(/(\w)(\w)\1/)
    while pos
      val=segment.match(/(\w)(\w)\1/,pos)
      if val and val[1]!=val[2]
        a,b=val[1,2]
        hypernet.each do |hseg|
          ssl|=hseg[b+a+b]
        end
        if ssl
          break
        end
      end
      pos=segment.index(/(\w)(\w)\1/,pos+1)
    end
  end
  if ssl
    count+=1
    next
  end
end
puts "Part 2: #{count} Addresses support SSL"