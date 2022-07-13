#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from openbabel import openbabel
from openbabel import pybel
from optparse import OptionParser


def squared_distance(coordsA, coordsB):
    """Find the squared distance between two 3-tuples"""
    sqrdist = sum( (a-b)**2 for a, b in zip(coordsA, coordsB) )
    return sqrdist
    
def rmsd(allcoordsA, allcoordsB):
    """Find the RMSD between two lists of 3-tuples"""
    deviation = sum(squared_distance(atomA, atomB) for 
                    (atomA, atomB) in zip(allcoordsA, allcoordsB))
    return math.sqrt(deviation / float(len(allcoordsA)))
    
if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-x", "--xtall", dest="xtall",
		      help="the reference (X-ray) structure")
    parser.add_option("-f", "--file",
		      dest="dockedposes",
		      help="File with structures to compare (eg. docking poses)")

    (options, args) = parser.parse_args()
    if not options.xtall:   # if filename is not given
      parser.error('Reference/Xtall structure not given')
    if not options.dockedposes:   # if filename is not given
      parser.error('Docked poses not given')

    #dockedposes = options.dockedposes
    #exit(1)

    # Read crystal pose
    crystal = next(pybel.readfile(options.xtall.split(".")[-1], options.xtall))

    # Find automorphisms involving only non-H atoms
    mappings = pybel.ob.vvpairUIntUInt()
    bitvec = pybel.ob.OBBitVec()
    lookup = []
    for i, atom in enumerate(crystal):
        if not atom.OBAtom.GetAtomicNum()==1:
            bitvec.SetBitOn(i+1)
            lookup.append(i)
    success = pybel.ob.FindAutomorphisms(crystal.OBMol, mappings, bitvec)

    # Find the RMSD between the crystal pose and each docked pose
    xtalcoords = [atom.coords for atom in crystal if not atom.OBAtom.GetAtomicNum()==1]
    for i, dockedpose in enumerate(pybel.readfile(options.dockedposes.split(".")[-1], options.dockedposes)):
        posecoords = [atom.coords for atom in dockedpose if not atom.OBAtom.GetAtomicNum()==1]
        minrmsd = 999999999999
        for mapping in mappings:
            automorph_coords = [None] * len(xtalcoords)
            for x, y in mapping:
                automorph_coords[lookup.index(x)] = xtalcoords[lookup.index(y)]
            mapping_rmsd = rmsd(posecoords, automorph_coords)
            if mapping_rmsd < minrmsd:
                minrmsd = mapping_rmsd
        #print("%s\t%i\t%s\t%.1f" % (options.xtall.split(".")[0], (i+1), dockedpose.title, minrmsd))
        print(("%i\t%.1f" % ( (i+1),  minrmsd)))