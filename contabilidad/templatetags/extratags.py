from django import template
from decimal import Decimal, ROUND_HALF_UP

register = template.Library()

@register.filter(name='percentage')
def percentage(fraction, population):
    try:
        return "%.2f%%" % ((float(fraction) / float(population)) * 100)
    except ValueError:
        return ''

@register.filter(name='pdb')
def pdb_filter(arg):
    import pdb; pdb.set_trace()
    

@register.filter
def validname(value):
    try:
        name = value['grouper']
        for r in value['list']:
            if r['pendiente'] == '*':
                return name + '*'
        return name
    except ValueError:
        return ''

@register.filter
def decimal_format(value,decimal_places=2):
    try:
        if value == '0':
            return value
        
        value = Decimal(str(round(value,decimal_places)))
        return moneyfmt(value,decimal_places,'')
    except ValueError:
        return ''

@register.filter
def sum_field(list,parameters):
    param = parameters.split(",")
    field = param[0]
    try:
        decimal_places = int(param[1])
    except:
         decimal_places = 0
    value = 0
    try:
        for row in list:
            value += row[field]
    except:
        pass
    
    return moneyfmt(Decimal(str(value)),decimal_places)


@register.simple_tag
def get_percent(list,columname, column,colvalue, universe):
    value = '0.00%'
    try:
        for item in list:
            if item[columname] == column:
                try:
                    population = item[universe]
                except:
                    population = universe
                                        
                try:
                    return "%.2f%%" % (((float(item[colvalue])) / float(population)) * 100)
                except ValueError:
                    return value        
    except:
        pass
    return value

@register.simple_tag
def get_value(list,columname, column,colvalue,decimal_places=2):   
    try: 
        for item in list:
            if item[columname] == column:
                return moneyfmt(Decimal(str(item[colvalue])),decimal_places)
    except:
        pass        
    return moneyfmt(Decimal('0'),decimal_places)

@register.simple_tag
def sum_value(list,columname, column,colvalue,decimal_places=2):
    value = Decimal(0)    
    try:
        for item in list:
            if item[columname] == column:
                value +=Decimal(str(item[colvalue]))
    except:
        pass
    return moneyfmt(value,decimal_places)

@register.simple_tag
def sum_percent(list,columname, column,colvalue,universe=None,universe_list=None, universe_columnname = None,universe_column=None ,universe_colvalue=None):
    value = Decimal(0)    
    try:        
        total = 0
        for item in list:
            total += Decimal(str(item[colvalue]))
            if item[columname] == column:
                value +=Decimal(str(item[colvalue]))
                
        
        if universe_list is not None:
            total = 0
            for item in universe_list:
                if item[universe_columnname] == universe_column:
                    total += Decimal(str(item[universe_colvalue]))
                     
            universe = total
            print universe
          
        elif universe is None:
            universe = total
        
        
        return "%.2f%%" % (((float(value)) / float(universe)) * 100)
    except Exception as ins:
        print unicode(ins)
        return "0.00%"
    
  
def moneyfmt( value, places = 4, curr = '', sep = ',', dp = '.', pos = '', neg = '-', trailneg = '' ):
    q = Decimal( 10 ) ** -places      # 2 places --> '0.01'
    sign, digits, _exp = value.quantize( q,rounding=ROUND_HALF_UP ).as_tuple()
    result = []
    digits = map( str, digits )
    build, next = result.append, digits.pop
    if sign:
        build( trailneg )
    for _i in range( places ):
        build( next() if digits else '0' )
    if places > 0:
        build( dp )
    if not digits:
        build( '0' )
    i = 0
    while digits:
        build( next() )
        i += 1
        if i == 3 and digits:
            i = 0        
            build( sep )
    build( curr )
    build( neg if sign else pos )
    return ''.join( reversed( result ) )
    
