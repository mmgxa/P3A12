from session12 import *
import pytest


##########################################
####  Polygon Sequence  - Class Test  ####
##########################################
def test_polygon_class():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.n_vertices == n, (f'actual: {p.n_vertices},'
                                   f' expected: {n}')
    assert p.n_edge == n, f'actual: {p.n_edge}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.int_angle == 60, (f'actual: {p.int_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.int_angle == 90, (f'actual: {p.int_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.edgelen, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edgelen},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.edgelen, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.int_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.edgelen, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.int_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


##########################################
######  Polygon Sequence  - Iters  #######
##########################################
def test_seq_iterable():
    polseq = PolySeq(3, 3)
    try:
        iter(polseq)
    except:
        assert False, 'Your Polygon Sequence for this week must be an iterable'


def test_seq_iterator():
    polseq = PolySeq(3, 3)
    try:
        next(iter(polseq))
    except:
        assert False, 'Your Polygon Sequence for this week must be an iterator'


############################################
##### Tests from Previous Week to show #####
#### that the PolySeq Class still works ####
############################################


##########################################
###########  Polygon Class  ##############
##########################################
def test_class_repr():
    '''
    Check for the __repr__ function for the Polygon Class
    '''
    pol = Polygon(3, 3)
    assert str(pol), "Your repr function is missing"


def test_class_eq():
    '''
    Check whether two same Polygons are deemed Equal
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(3, 3)
    assert pol1 == pol2, 'Your equality function is bogus'


def test_class_neq():
    '''
    Check whether two same Polygons are deemed Equal
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert pol1 != pol2, 'Your equality function is bogus'


def test_class_gr():
    '''
    Check if one Polygon is greather than other
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert pol1 < pol2, 'Your greater function is bogus'


def test_class_ngr():
    '''
    Check if one Polygon is greather than other
    '''
    pol1 = Polygon(3, 3)
    pol2 = Polygon(4, 3)
    assert (pol1 > pol2) == False, 'Your greater function is bogus'


def test_class_prop():
    '''
    Check for the existence of the properties mentioned in the assignment
    '''
    pol = Polygon(3, 3)
    for prop in ['n_edge', 'circumradius', 'int_angle', 'edgelen', 'apothem', 'area', 'perimeter']:
        assert getattr(
            pol, prop), 'At least one of the required attributes is missing!'


##########################################
##########  Polygon Sequence  ############
##########################################
def test_seq_repr():
    '''
    Check for the __repr__ function for the Polygon Sequence
    '''
    polseq = PolySeq(3, 3)
    assert str(polseq), "Your repr function is missing"


def test_seq_prop():
    '''
    Check for the existence of the properties mentioned in the assignment
    '''
    polseq = PolySeq(3, 3)
    assert getattr(
        polseq, 'max_effic'), 'The maximum efficiency property is missing!'

def test_seq_iterable():
    '''
    Check whether the Polygon Sequence is an iterator or not
    '''
    polseq = PolySeq(3, 3)
    assert ('__next__' in dir(polseq)) == False, "Your Sequence is an iterator!"
    assert '__iter__' in dir(polseq), "Your Sequence is not an iterable"
    assert '__next__' in dir(polseq.PolySeqIter), "Your Sequence Iterator is not an iterator"
    assert '__iter__' in dir(polseq.PolySeqIter), "Your Sequence Iterator is not an iterator"