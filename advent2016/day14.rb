require 'digest'
input=ARGV[0]
md5=Digest::MD5.new
keys=[]
num=0
while keys.length<64
  c=md5.hexdigest(input+num.to_s).match(/([[:xdigit:]])\1{2}/)
  if c
    re=Regexp.new(c[1]*5)
    d=((num+1)..(num+1000)).map{ |n| md5.hexdigest(input+n.to_s).match(re) }.any?
    if d
      keys<<md5.hexdigest(input+num.to_s)
      #puts "Key %02d: %s (%d)" % [keys.length,keys[-1],num]
    end
  end
  num+=1
end
puts "Part 1: 64th key found at index #{num-1}"
keys=[]
alldigests=[]
num=0
(0...1000).each do |n|
  cdigest=md5.hexdigest(input+n.to_s)
  2016.times{ cdigest=md5.hexdigest(cdigest) }
  alldigests<<cdigest
end
while keys.length<64
  cdigest=md5.hexdigest(input+(num+1000).to_s)
  2016.times{ cdigest=md5.hexdigest(cdigest) }
  alldigests<<cdigest
  if /([[:xdigit:]])\1\1/=~alldigests[num]
    if alldigests[num+1,1000].any?{ |digest| digest[$1*5] }
      keys<<alldigests[num]
      #puts "Key %02d: #{keys[-1]} (#{num})" % [keys.length]
    end
  end
  num+=1
end
puts "Part 2: 64th key found at index #{num-1}"
