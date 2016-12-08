class Display
  def initialize(grid)
    x,y=grid
    @lit=0
    @display=Array.new(y) { Array.new(x,:off) }
  end
  def command(cmdstring)
    case cmdstring.split(' ')[0]
    when 'rect'
      x,y=cmdstring.split(' ')[1].split('x')
      x=x.to_i
      y=y.to_i
      (0...y).each do |i|
        (0...x).each do |j|
	  if @display[i][j]==:off
            @display[i][j]=:on
	    @lit+=1
	  end
        end
      end
    when 'rotate'
      if cmdstring.split(' ')[2][0]=='x'
        column=cmdstring.split(' ')[2].split('=')[1].to_i
	n=cmdstring.split(' ')[4].to_i
	temp=@display.transpose
        temp[column].rotate!(-n)
	@display=temp.transpose
      elsif cmdstring.split(' ')[2][0]=='y'
        row=cmdstring.split(' ')[2].split('=')[1].to_i
	n=cmdstring.split(' ')[4].to_i
	@display[row].rotate!(-n)
      end
    end
  end
  def print(off,on)
    @display.each do |row|
      s=''
      row.each do |c|
        if c==:off
	  s+=off
	elsif c==:on
	  s+=on
	end
      end
      puts "#{s}"
    end
  end
  attr_accessor :lit
end

f=File.open(ARGV[0])
lines=f.readlines()
#d=Display.new([7,3])
d=Display.new([50,6])
lines.each do |line|
  d.command(line.strip)
end
puts "Part 1: #{d.lit} lit pixels"
d.print('.','#')
