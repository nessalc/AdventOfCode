class Grid
  def initialize(initial_pos,grid=nil)
    @x,@y=initial_pos
    @grid=grid
    return @x,@y
  end
  attr_accessor :x
  attr_accessor :y
  def pos
    return @x, @y
  end
  def value
    if @grid
      return @grid[@y][@x]
    else
      return @x, @y
    end
  end
  def set_grid(array)
    @grid=array
    return @grid
  end
  def direction_valid(direction)
    unless @grid then
      return true
    else
      if direction==:up and not @y==0 then
        return (@grid[@y-1][@x] != nil)
      elsif direction==:down and not @y==(@grid.length-1) then
        return (@grid[@y+1][@x] != nil)
      elsif direction==:left and not @x==0 then
        return (@grid[@y][@x-1] != nil)
      elsif direction==:right and not @x==(@grid[@y].length-1) then
        return (@grid[@y][@x+1] != nil)
      end
      return false
    end
  end
  def move(direction,distance=1)
    if direction_valid(direction)
      if direction==:up then
        @y-=distance
      elsif direction==:down then
        @y+=distance
      elsif direction==:left then
        @x-=distance
      elsif direction==:right then
        @x+=distance
      end
    end
  end
end

f=File.open(ARGV[0])
directions=f.readlines

code=''
keypad=Grid.new([1,1])
keypad.set_grid([[1,2,3],[4,5,6],[7,8,9]])
directions.each do |d|
  d.chars.each do |c|
    case c
    when 'U'
      keypad.move(:up)
    when 'D'
      keypad.move(:down)
    when 'L'
      keypad.move(:left)
    when 'R'
      keypad.move(:right)
    when "\n"
      code+=keypad.value.to_s
    end
  end
end
code+=keypad.value.to_s
puts "Part 1: #{code}"

code=''
keypad=Grid.new([0,2])
keypad.set_grid([[nil, nil, 1, nil, nil],[nil, 2, 3, 4, nil],[5, 6, 7, 8, 9],[nil, 'A', 'B', 'C', nil],[nil, nil, 'D', nil, nil]])
directions.each do |d|
  d.chars.each do |c|
    case c
    when 'U'
      keypad.move(:up)
    when 'D'
      keypad.move(:down)
    when 'L'
      keypad.move(:left)
    when 'R'
      keypad.move(:right)
    when "\n"
      code+=keypad.value.to_s
    end
  end
end
code+=keypad.value.to_s
puts "Part 1: #{code}"
