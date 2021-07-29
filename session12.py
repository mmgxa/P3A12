import math


##################################################
###########       The Polygon Class    ###########
##################################################
class Polygon:
    '''
    A Polygon Class which is intitialized with number of edges and its circumradius.

    Its properties such as interior angle, edge lengths, apothem, area, and perimeter are calculated,
    and can be accessed as key (p['n_edge']) or as property (p.n_edge).

    The former will give a soft warning and continue for a wrong key; the latter will halt if 
    the incorrect property is asked.
    '''

    def __init__(self, n_edge: int, circumradius: int) -> None:

        if n_edge < 3:
            raise ValueError(
                'The number of edges must be atleast 3 for a Polygon!')

        if circumradius < 0:
            raise ValueError(
                'The circumradius of a Polygon cannot be negative!')

        self.n_edge_i = n_edge
        self.circumradius_i = circumradius
        self.int_angle_i = None
        self.edgelen_i = None 
        self.apothem_i = None
        self.area_i = None
        self.perimeter_i = None

    @property
    def n_vertices(self):
        return self.n_edge_i

    @property
    def n_edge(self) -> int:
        return self.n_edge_i

    @property
    def circumradius(self) -> int:
        return self.circumradius_i

    @property
    def int_angle(self) -> float:
        if self.int_angle_i is not None:
            return self.int_angle_i
        else:
            self.int_angle_i = (self.n_edge - 2)*(180/self.n_edge)
            return self.int_angle_i

    @property
    def edgelen(self) -> float:
        if self.edgelen_i is not None:
            return self.edgelen_i
        else:
            self.edgelen_i = round(2*self.circumradius*math.sin(math.pi/self.n_edge), 3)
            return self.edgelen_i

    @property
    def apothem(self) -> float:
        if self.apothem_i is not None:
            return self.apothem_i
        else:
            self.apothem_i = round(self.circumradius * math.cos(math.pi/self.n_edge), 3)
            return self.apothem_i

    @property
    def area(self) -> float:
        if self.area_i is not None:
            return self.area_i
        else:
            self.area_i = round(0.5*self.n_edge * self.edgelen * self.apothem, 3)
            return self.area_i

    @property
    def perimeter(self) -> float:
        if self.perimeter_i is not None:
            return self.perimeter_i
        else:            
            self.perimeter_i = round(self.n_edge * self.edgelen, 3)
            return self.perimeter_i

    def __getitem__(self, str):
        '''
        What to return when the properties of the object is passed as key 
        '''
        try:
            print(getattr(self, str))
        except AttributeError:
            print(
                'Key must be one of these: n_edge/circumradius/int_angle/edgelen/apothem/area/perimeter')

    def __repr__(self) -> str:
        '''
        How the output appears when the object is printed.
        '''
        return f'Polygon(n={self.n_edge_i}, R={self.circumradius_i})'
        

    def __eq__(self, other):
        '''
        This compares two objects based on the Polygon Class based on their
        number of edges and circumradius ...
        '''
        if not isinstance(other, Polygon):
            raise TypeError(
                f'Second argument: Expected {type(self)} ; Found {type(other)}')
        return (self.n_edge == other.n_edge) and (self.circumradius == other.circumradius)

    def __gt__(self, other):
        '''
        This compares two objects based on the Polygon Class based on their
        number of edges only!
        '''
        if not isinstance(other, Polygon):
            raise TypeError(
                f'Second argument: Expected {type(self)} ; Found {type(other)}')
        return self.n_edge > other.n_edge


##################################################
#########       The Polygon Sequence    ##########
##################################################

class PolySeq():
    def __init__(self, max_edges: int, common_circumradius: int):

        if max_edges < 3:
            raise ValueError(
                'The maximum number of edges must be atleast 3 for any Polygon!')

        if common_circumradius <= 0:
            raise ValueError(
                'The common circumradius of a Polygon cannot be negative!')

        self.max_edges = max_edges
        self.common_circumradius = common_circumradius

        self.polygons = [Polygon(i, common_circumradius) for i in range(3, max_edges+1)]


    def __repr__(self) -> str:
        '''
        How the output appears when the object is printed.
        '''
        return (f'This Polygon Sequence contains polygons with the following properties:' + f'\n'
                f'\t' + f'Sides: From 3 to {self.max_edges},' + f'\n'
                f'\t' + f'Common circumradius = {self.common_circumradius},')

    @property
    def max_effic(self):
        sorted_polygons = sorted(self.polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    def __iter__(self):
        '''
        This method returns the iterator sub-class
        '''
        return self.PolySeqIter(self.max_edges, self.common_circumradius)

    class PolySeqIter:
        '''
        This is an iterator implemented as a sub-class
        '''

        def __init__(self, max_edges, common_circumradius):
            self.max_edges = max_edges
            self.common_circumradius = common_circumradius
            self.i = 3

        def __len__(self):
            return self.max_edges - 2

        def __iter__(self):
            return self

        def __next__(self):
            if self.i > self.max_edges:
                raise StopIteration
            else:
                pol = Polygon(self.i, self.common_circumradius)
                self.i += 1
                return pol
