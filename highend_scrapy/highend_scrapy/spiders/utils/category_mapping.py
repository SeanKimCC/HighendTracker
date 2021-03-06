def map_category(category):
	ACC = "ACCESSORIES"
	BELTS = "BELTS"
	EYEWEAR = "EYEWEAR"

	####   HATS #
	HATS = "HATS"
	CAPS = "CAPS"
	BEANIES = "BEANIES"
	####   HATS #

	####   JEWELRY #
	JEWELRY = "JEWELRY"
	BRACELETS = "BRACELETS"
	EARRINGS = "EARRINGS"
	NECKLACES = "NECKLACES"
	RINGS = "RINGS"
	####   JEWELRY #

	# ACCESSORIES #

	# BAGS #
	BAGS = "BAGS"
	BACKPACKS = "BACKPACKS"
	BRIEFCASES = "BRIEFCASES"
	DUFFLE_BAGS = "DUFFLE BAGS"
	MESSENGER_BAGS = "MESSENGER BAGS"
	POUCHES = "POUCHES"
	TOTE_BAGS = "TOTE BAGS"
	TRAVEL_BAGS = "TRAVEL BAGS"
	# BAGS #

	# CLOTHINGS #
	CLOTHING = "CLOTHING"

	####    TOP #
	TOP = "TOP"
	SUITS_BLAZERS = "SUITS & BLAZERS"

	#######     JACKETS #
	JACKETS = "JACKETS"
	DENIM_JACKETS = "DENIM JACKETS"
	LEATHER_JACKETS = "LEATHER JACKETS"
	DOWN_JACKETS = "DOWN JACKETS"
	FUR_SHEARLING = "FUR & SHEARLING"
	#######     JACKETS #

	#######     COATS #
	COATS = "COATS"
	PEA_COATS = "PEA COATS"
	LONG_COATS = "LONG COATS"
	TRENCH_COATS = "TRENCH COATS"
	#######     COATS #

	SHIRTS = "SHIRTS"

	#######     SWEATERS #
	SWEATERS = "SWEATERS"
	CARDIGANS = "CARDIGANS"
	CREWNECKS = "CREWNECKS"
	HOODIES = "HOODIES"
	SWEATSHIRTS = "SWEATSHIRTS"
	TURTLENECKS = "TURTLENECKS"
	V_NECKS = "V-NECKS"
	#######     SWEATERS #

	T_SHIRTS = "T-SHIRTS"
	TANK_TOPS = "TANK TOPS"
	POLOS = "POLOS"
	####    TOP #

	####   BOTTOM #
	BOTTOM = "BOTTOM"
	JEANS = "JEANS"
	SHORTS = "SHORTS"

	#######     PANTS #
	PANTS = "PANTS"
	CARGO_PANTS = "CARGO PANTS"
	LEATHER_PANTS = "LEATHER_PANTS"
	SWEATPANTS = "SWEATPANTS"
	TROUSERS = "TROUSERS"
	#######     PANTS #

	####   BOTTOM #
	# CLOTHINGS #

	# SHOES #
	SHOES = "SHOES"
	SNEAKERS = "SNEAKERS"
	BOOTS = "BOOTS"
	LACE_UPS = "LACE UPS"
	LOAFERS = "LOAFERS"
	SANDALS = "SANDALS"
	# SHOES #

	categories = {
		'accessories': ACC,
		'bags': BAGS,
		'jackets': JACKETS,
		'coats': COATS,
		'jeans': JEANS,
		'pants': PANTS,
		'shirts': SHIRTS,
		'shorts': SHORTS,
		'suits-blazers': SUITS_BLAZERS,
		'cardigans': CARDIGANS,
		'crewnecks': CREWNECKS,
		'hoodies-zipups': HOODIES,
		'sweatshirts': SWEATSHIRTS,
		'turtlenecks':TURTLENECKS,
		't-shirts': T_SHIRTS,
		'shoes': SHOES
	}

	return categories[category]




