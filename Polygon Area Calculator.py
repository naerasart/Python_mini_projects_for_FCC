class Rectangle:
   
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, value):
    self.width = value
  
  def set_height(self, value):
    self.height = value

  def get_area(self):
    return(self.width * self.height)
  
  def get_perimeter(self):
    return(2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** (1/2))

  def get_picture(self):
    if self.width  > 50 :
      return("Too big for picture.")
    elif self.height > 50:
      return("Too big for picture.")
    elif self.height <= 50:
      return( ( ("*" * self.width)+ "\n" ) * self.height)
    elif self.width <= 50:
      return( ( ("*" * self.width)+ "\n" ) * self.height)
  
  
  def get_amount_inside(self, square):
    if self.width < square.width :
      return int()
    elif  self.height < square.height:
      return int()
    elif  self.width >= square.width:
      return( self.get_area() // square.get_area() )
    elif  self.height >= square.height:  
      return( self.get_area() / square.get_area() )
     
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
  def __init__(self, length):
    Rectangle.width = length
    Rectangle.height = length

  def set_width(self, value):
    self.set_side(value)

  def set_height(self, value):
    self.set_side(value)

  def set_side(self, value):
    Rectangle.set_width(self, value)
    Rectangle.set_height(self, value)

  def __str__(self):
    return f"Square(side={self.width})"

  

 