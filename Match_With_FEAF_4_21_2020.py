#!/usr/bin/env python

# This program matches the products found in a file named: Products 10-31-18.txt
# against an Augmented FEA Taxonomy maintained in a file named Product_Taxonomy_1_25_2018.txt  
# It puts the products it can't match into a file names something like: "Not FEAF Aligned 17 56 38 31-10-2018.txt"
# It puts the products it can align into a file named "FEAF Alignment 17 56 38 31-10-2018.txt"

import os;
import socket;
import sys;
import time;

# Edit these file names as appropriate
TaxonomyFile = "Taxonomy 4-21-2020.txt"
ProductInventory = "counted.txt"
ad = dict() # ad = argument dictionary to be used throughout this script.

def main():

   if __name__ != "__main__": return None
   
   ad = initialize_argument_dictionary()

   nl = ad["nl"]

   t1 = ad["start time"]

   print ad["program fn"] + " is running,"

   display_program_filenames( ad )

   ad["tl"] = load_taxonomy_list( ad, ad["tax fn"] )

# open the output hits file.
   ad["hits f"] = open( ad["hits fn"], "w" )

# open the output misses file.
   ad["misses f"] = open( ad["misses fn"], "w" )

   process_inventory_file( ad, ad["inventory fn"] )

# we are done with these files so close them.
   ad["hits f"].close()

   ad["misses f"].close()

   t2 = time.time()

   t3 = t2 - t1

   z = "Done in %1.3f seconds.%s%s" %(t3,bells( 3 ),new_line())

   sys.stdout.write( z )

   return None
# main()


def display_program_filenames( ad ):

   kl = ad.keys()

   kl.sort()

   print "Current working directory: " + os.getcwd()

   print "Name of files to be processed:"

   for ks in kl:
      if " fn" in ks: print "File (%s) = %s" %(ks,ad[ks])
# end of for ks in kl: loop.

   return None
# display_program_filenames()

def load_taxonomy_list( ad, tax_fn ):
   """This function loads the specified taxonomy file (tax_fn)\
      into a list of strings whose fields are delimited by tab characters."""

   tab_character = tab()

# tf = taxonomy file object
   tf = open( tax_fn, "r" )

# tl = taxonomy list
   tl = map( str.strip, tf.readlines() )

   tf.close()

# netl = new edited taxonomy list
   netl = list()

   min_len = 3

   for i in xrange( len( tl ) ):
      xl = tl[i].split(tab())
# ts = taxonomy string
      ts = tl[i]
      xl= ts.split( tab() )
      if len( xl ) < min_len: continue
      EA_index = xl[0].strip()
      the_category = xl[1].strip()
      product_name = xl[2].strip()

# format the tab delimited taxonomy string (ts).
      ts = product_name + tab_character + EA_index + tab_character + the_category

# save the taxonomy string.
      netl.append(ts)

# end of for i in xrange( len( tl ) ): loop.

# Return the loaded taxonomy list (tl) to the caller.
   return netl
# load_taxonomy_list()


def process_inventory_file( ad, inventory_fn ):

   nl = new_line()

   tab_character = tab()

   inventory_f = open( inventory_fn, "r" )

   while True:
      inventory_s = inventory_f.readline()
      if len( inventory_s ) == 0: break # EOF?
      product_name = inventory_s.strip()
      product_in_taxonomy, tax_s, inv_s = search_taxonomy_for_product_name( ad, product_name, inventory_s )

# save this product data in the appropriate file.
      if product_in_taxonomy:  
         ad["hits f"].write( format_tax_data(tax_s, product_name) + nl )
      else:
         ad["misses f"].write( inv_s )

# end of while True: loop.

   inventory_f.close()

   return None
# process_inventory_file()


def search_taxonomy_for_product_name( ad, inv_product_name,file_data_s ):

# tc = tab character
   tc = tab()

# search/process the taxonomy list looking for the product name.
# ts = taxonomy string
   inv_product_name = inv_product_name.lower()

   product_found = False

   for ts in ad["tl"]:
      xs = ts.lower()
      xl = xs.split(tc)
      tax_product_name = xl[0]
      if tax_product_name == 'r': tax_product_name = space()+tax_product_name+space()
      product_found = tax_product_name in inv_product_name
      if product_found: break
# end of for ts in ad["tl"]: loop.

# determine what to return to the caller.
   if product_found:
      return product_found, ts, None
   else:
      return product_found, None, file_data_s
# end of search_taxonomy_for_product_name()

def format_tax_data(tax_s, inv_product_name):
   tc = tab()
   xl = tax_s.split( tc )
   tax_product_name = xl[0]
   tax_ea_index = xl[1]
   tax_category = xl[2]
   ms = tax_product_name
   tax_s = tax_ea_index+tc+tax_category+tc+inv_product_name+tc+ms
   return tax_s
# end of format_tax_data()

def initialize_argument_dictionary():

   global ad;

   ad = dict()

   av = ad["av"] = ad["argv"] = sys.argv

   ac = len( av )

   ad["ac"] = ad["argc"] = ac

   ad["start time"] = time.time()

   timeStamp = time.strftime(" %H %M %S %d-%m-%Y")


# use the program filename to help make the names of the hits and misses files.
   prog_fn = os.path.basename( ad["av"][0] )

   ad["program fn"] = prog_fn
      
   ad["hits fn"] = "FEAF Alignment"+timeStamp+".txt"
   ad["misses fn"] = "Not FEAF Aligned"+timeStamp+".txt"

   ad["nl"] = new_line()

# use Product_taxonomy.txt
   ad["tax fn"] = TaxonomyFile

   ad["inventory fn"] = ProductInventory

   return ad
# end of initialize_argument_dictionary()


def bell():

   return "\a"
# bell()


def new_line():

   return os.linesep
# new_line()


def space():

   return ' '
# space()


def tab():

   return "\t"
# tab()


def bells( num_bells = 1 ):

   if num_bells < 0: num_bells = 0

   if num_bells > 5: num_bells = 5

   return bell() * num_bells
# bells()


# the main logic of this script starts here.
main()
