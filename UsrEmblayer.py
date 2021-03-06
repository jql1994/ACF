__author__ = 'jingyuan'
import numpy
import theano
import cPickle

class UsrEmblayer(object):
    def __init__(self, rng, n_usr, dim, name, prefix=None):
        self.name = name

        if prefix == None:
            U_values = numpy.zeros((n_usr, dim),dtype=numpy.float32)
            U = theano.shared(value=U_values, name='U', borrow=True)
        else:
            f = file(prefix + name + '.save', 'rb')
            U = cPickle.load(f)
            f.close()

        self.U = U
        self.output = self.U
        self.params = [self.U]

    def save(self, prefix):
        f = file(prefix + self.name + '.save', 'wb')
        for obj in self.params:
            cPickle.dump(obj, f, protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()