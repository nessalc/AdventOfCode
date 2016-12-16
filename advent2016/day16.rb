size=ARGV[0].to_i
input=ARGV[1]
data=input
puts "Processing data..."
while data.length<size
  a=data
  b=data.reverse.tr('10','01')
  data=a+'0'+b
  puts data.length
end
data=data[0...size]
checksum=data
puts "Calculating checksum..."
while checksum.length%2==0
  temp=''
  checksum.scan(/../) do |m|
    if m=='00' or m=='11'
      temp<<'1'
    else
      temp<<'0'
    end
    if temp.length%1000000==0
      putc "."
    end
  end
  checksum=temp
  puts checksum.length
end
#puts "Data: #{data}"
puts "Checksum: #{checksum}"
