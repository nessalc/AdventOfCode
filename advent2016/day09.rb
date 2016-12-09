f=File.open(ARGV[0])
lines=f.readlines()
def decompressed_length(instring,method=1)
  len=0
  pos=instring.index(/\(\d+x\d+\)/)
  while pos
    len+=pos
    val=instring.match(/\((\d+)x(\d+)\)/)
    if instring[val[0].length+pos,val[1].to_i].index(/\(\d+x\d+\)/)
      if method==1
        len+=instring[val[0].length+pos,val[1].to_i].length*val[2].to_i
      else
        len+=decompressed_length(instring[val[0].length+pos,val[1].to_i],method)*val[2].to_i
      end
    else
      len+=val[1].to_i*val[2].to_i
    end
    instring=instring[val[0].length+pos+val[1].to_i,instring.length]
    pos=instring.index(/\(\d+x\d+\)/)
  end
  len+=instring.length
  return len
end
lines.each do |line|
  line.strip!
  len=decompressed_length(line)
  #r=''
  #pos=line.index(/\(\d+x\d+\)/)
  #while pos
  #  val=line.match(/\((\d+)x(\d+)\)/)
  #  r+=line[0,pos]+(line[val[0].length+pos,val[1].to_i]*val[2].to_i)
  #  line=line[val[0].length+pos+val[1].to_i,line.length]
  #  pos=line.index(/\(\d+x\d+\)/)
  #end
  #r+=line
  #puts "Part 1: Length of decompressed output is #{r.length}"
  puts "Part 1: Length of decompressed output is #{len}"
end
lines.each do |line|
  line.strip!
  len=decompressed_length(line,2)
  puts "Part 2: Length of decompressed output is #{len}"
end
