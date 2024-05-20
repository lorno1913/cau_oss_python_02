'''
클래스
Line: 외부에서 접근 불가능한 필드 __length가 있으며, 기본 값은 1이다.
      생성자를 통해 초기 __length의 값을 지정할 수 있으며, 해당 필드에 접근하기위한 set_length,get_length메소드가 있다.

함수
area_square: Line클래스의 객체를 매개변수로 받아, length*length의 정사각형의 넓이를 반환한다.
area_circle: Line클래스의 객체를 매개변수로 받아, length*length*pi의 원의 넓이를 반환한다.
area_regualr_triangle: Line클래스의 객체를 매개변수로 받아, length*length*sqrt(3)/4의 정삼각형의 넓이를 반환한다.
'''

import math


class Line:
    '''
    외부에서 접근 불가능한 필드인 __length가 있으며, 기본 값은 1 이다.
    생성자를 통해 초기 length값을 지정할 수 있다.
    해당 필드에 접근하기 위해서는 set_length,get_length를 이용하면 된다.
    '''
    __length =None


    def __init__(self, initial_value=1):
        ''' 생성자를 통해 초기 __length의 값을 지정한다.
          __length 필드는 int 또는 float타입으로만 설정될 수 있으며, 0보다 큰 값만을 받는다.
          만약, 타입이 int or float이 아니거나 0보다 작은 값을 전달 받으면 기본값인 1을 유지한다.
        Args:
            initial_value: 수정할 length값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> obj = line (10) #생성자를 통해 __length의 값이 10으로 변경된다.
            >>> obj = line (0)  #기본값인 1을 유지한다.
        '''
        if type(initial_value) == int or float:
            if initial_value > 0:
                self.__length = initial_value

    def set_length(self, value):
        '''__length의 값을 n으로 변경한다.
        __length 필드는 int 또는 float타입으로만 설정될 수 있으며, 0보다 큰 값만을 받는다.
        만약, 타입이 int or float이 아니거나 0보다 작은 값을 전달 받으면 이전 값 유지한다
        Args:
            value: n으로 변경할 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> obj.set_length(10) # __length의 값이 10으로 변경된다.
            >>> obj.set_length(0)  #이전 값을 유지한다.
        '''
        if type(value) == int or float:
            if value > 0:
                self.__length = value
    
    def get_length(self):
        '''__length의 값을 반환한다.
        Args:
            아무 값도 받지 않음 (혹은 공란으로 비워둠)
        Returns:
            __length
        Examples:
            >>> obj.get_length() # __length의 값을 반환한다.
        '''
        return self.__length


 
    
def area_square(value_get_length):
    '''value_get_length의 값을 매개변수 삼아, value_get_length를 한변으로 하는 정사각형의 넓이를 반환
    만약, 매개변수의 타입이 Line 클래스가 아닐경우 0을 반환
    Parameters
    ----------
       value_get_length: 정사각형의 한변의 길이
    Returns
    -------
        value_get_length * value_get_length
    Example
    -------
        >>> ret = aera_square(10) #한변의 길이가 10인 정사각형의 넓이를 반환
    '''
    if isinstance(value_get_length, Line):
        return value_get_length.get_length()**2
    else:
        return 0
    
  
  



def area_circle(value_get_length):
    '''value_get_length의 값을 매개변수 삼아, value_get_length를 반지름으로 하는 원의 넓이를 반환
    만약, 매개변수의 타입이 Line 클래스가 아닐경우 0을 반환
    Parameters
    ----------
       value_get_length: 원의 반지름의 길이
    Returns
    -------
        value_get_length * value_get_length * pi
    Example
    -------
        >>> ret = aera_circle(10) #반지름의 길이가 10인 원의 넓이를 반환
    '''
    
    if isinstance(value_get_length, Line):
        return value_get_length.get_length()**2*math.pi
    else:
        return 0
   



def area_regular_triangle(value_get_length):
    '''value_get_length의 값을 매개변수 삼아, value_get_length를 한변으로 하는 정삼각형의 넓이를 반환
    만약, 매개변수의 타입이 Line 클래스가 아닐경우 0을 반환
    Parameters
    ----------
       value_get_length: 정삼각형의 한변의 길이
    Returns
    -------
        value_get_length * value_get_length*sqrt(3)/4
    Example
    -------
        >>> ret = aera_regular_triangle(10) #한변의 길이가 10인 정삼각형의 넓이를 반환
    '''
    
    if isinstance(value_get_length, Line):
        return value_get_length.get_length()**2*math.sqrt(3)/4
    else:
        return 0
 



