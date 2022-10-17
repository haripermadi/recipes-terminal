# RECIPES with input from terminal
# import requests
# https://www.themealdb.com/api.php == food recipe api
# list recipes , dictionary? name:[ingredients]
categories = {
  "Beef": ["Beef and Mustard Pie", "Beef Bourguignon", "Beef Rendang", "Beef Wellington", "Steak and Kidney Pie"],
  "Chicken": ["Brown Stew Chicken", "Chicken & mushroom Hotpot", "Chicken Karaage", "French Onion Chicken with Roasted Carrots & Mashed Potatoes", "Teriyaki Chicken Casserole"],
  "Dessert": ["Apple & Blackberry Crumbl", "Banana Pancakes", "Bread and Butter Pudding", "Carrot Cake", "Chocolate Raspberry Brownies"],
  "Lamb": ["Lamb and Lemon Souvlaki"],
  "Miscellaneous": ["Bean & Sausage Hotpot", "French Lentils With Garlic and Thyme", "Pizza Express Margherita", "Poutine"],
  "Pasta": ["Spaghetti alla Carbonara"],
  "Pork": ["BBQ Pork Sloppy Joes"],
  "Seafood": ["Baked salmon with fennel & tomatoes", "Cajun spiced fish tacos", "Fish pie", "Honey Teriyaki Salmon", "Kung Po Prawns"],
  "Side": ["Boulangère Potatoe"],
  "Starter": ["Cream Cheese Tart", "Broccoli & Stilton soup"],
  "Breakfast": ["Breakfast Potatoes", "Full English Breakfast", "Salmon Eggs Eggs Benedict"],
}
descriptions = {
  "Beef": "Beef is the culinary name for meat from cattle, particularly skeletal muscle. Humans have been eating beef since prehistoric times.[1] Beef is a source of high-quality protein and essential nutrients.[2]",
  "Chicken":  "Chicken is a type of domesticated fowl, a subspecies of the red junglefowl. It is one of the most common and widespread domestic animals, with a total population of more than 19 billion as of 2011.[1] Humans commonly keep chickens as a source of food (consuming both their meat and eggs) and, more rarely, as pets.",
  "Dessert": "Dessert is a course that concludes a meal. The course usually consists of sweet foods, such as confections dishes or fruit, and possibly a beverage such as dessert wine or liqueur, however in the United States it may include coffee, cheeses, nuts, or other savory items regarded as a separate course elsewhere. In some parts of the world, such as much of central and western Africa, and most parts of China, there is no tradition of a dessert course to conclude a meal.\r\n\r\nThe term dessert can apply to many confections, such as biscuits, cakes, cookies, custards, gelatins, ice creams, pastries, pies, puddings, and sweet soups, and tarts. Fruit is also commonly found in dessert courses because of its naturally occurring sweetness. Some cultures sweeten foods that are more commonly savory to create desserts.",
  "Lamb": "Lamb, hogget, and mutton are the meat of domestic sheep (species Ovis aries) at different ages.\r\n\r\nA sheep in its first year is called a lamb, and its meat is also called lamb. The meat of a juvenile sheep older than one year is hogget; outside the USA this is also a term for the living animal. The meat of an adult sheep is mutton, a term only used for the meat, not the living animals. The term mutton is almost always used to refer to goat meat in the Indian subcontinent.\r\n\r\n",
  "Miscellaneous": "General foods that don't fit into another category",
  "Pasta": "Pasta is a staple food of traditional Italian cuisine, with the first reference dating to 1154 in Sicily.\r\n\r\nAlso commonly used to refer to the variety of pasta dishes, pasta is typically a noodle made from an unleavened dough of a durum wheat flour mixed with water or eggs and formed into sheets or various shapes, then cooked by boiling or baking. As an alternative for those wanting a different taste, or who need to avoid products containing gluten, some pastas can be made using rice flour in place of wheat.[3][4] Pastas may be divided into two broad categories, dried (pasta secca) and fresh (pasta fresca).",
  "Pork": "Pork is the culinary name for meat from a domestic pig (Sus scrofa domesticus). It is the most commonly consumed meat worldwide,[1] with evidence of pig husbandry dating back to 5000 BC. Pork is eaten both freshly cooked and preserved. Curing extends the shelf life of the pork products. Ham, smoked pork, gammon, bacon and sausage are examples of preserved pork. Charcuterie is the branch of cooking devoted to prepared meat products, many from pork.\r\n\r\nPork is the most popular meat in Eastern and Southeastern Asia, and is also very common in the Western world, especially in Central Europe. It is highly prized in Asian cuisines for its fat content and pleasant texture. Consumption of pork is forbidden by Jewish and Muslim dietary law, a taboo that is deeply rooted in tradition, with several suggested possible causes. The sale of pork is limited in Israel and illegal in certain Muslim countries.",
  "Seafood": "Seafood is any form of sea life regarded as food by humans. Seafood prominently includes fish and shellfish. Shellfish include various species of molluscs, crustaceans, and echinoderms. Historically, sea mammals such as whales and dolphins have been consumed as food, though that happens to a lesser extent in modern times. Edible sea plants, such as some seaweeds and microalgae, are widely eaten as seafood around the world, especially in Asia (see the category of sea vegetables). In North America, although not generally in the United Kingdom, the term \"seafood\" is extended to fresh water organisms eaten by humans, so all edible aquatic life may be referred to as seafood. For the sake of completeness, this article includes all edible aquatic life.",
  "Side": "A side dish, sometimes referred to as a side order, side item, or simply a side, is a food item that accompanies the entrée or main course at a meal. Side dishes such as salad, potatoes and bread are commonly used with main courses throughout many countries of the western world. New side orders introduced within the past decade[citation needed], such as rice and couscous, have grown to be quite popular throughout Europe, especially at formal occasions (with couscous appearing more commonly at dinner parties with Middle Eastern dishes).",
  "Starter": "An entrée in modern French table service and that of much of the English-speaking world (apart from the United States and parts of Canada) is a dish served before the main course of a meal; it may be the first dish served, or it may follow a soup or other small dish or dishes. In the United States and parts of Canada, an entrée is the main dish or the only dish of a meal.\r\n\r\nHistorically, the entrée was one of the stages of the “Classical Order” of formal French table service of the 18th and 19th centuries. It formed a part of the “first service” of the meal, which consisted of potage, hors d’œuvre, and entrée (including the bouilli and relevé). The “second service” consisted of roast (rôti), salad, and entremets (the entremets sometimes being separated into a “third service” of their own). The final service consisted only of dessert.[3]:3–11 :13–25",
  "Vegan": "Veganism is both the practice of abstaining from the use of animal products, particularly in diet, and an associated philosophy that rejects the commodity status of animals.[b] A follower of either the diet or the philosophy is known as a vegan (pronounced /ˈviːɡən/ VEE-gən). Distinctions are sometimes made between several categories of veganism. Dietary vegans (or strict vegetarians) refrain from consuming animal products, not only meat but also eggs, dairy products and other animal-derived substances.[c] The term ethical vegan is often applied to those who not only follow a vegan diet but extend the philosophy into other areas of their lives, and oppose the use of animals for any purpose.[d] Another term is environmental veganism, which refers to the avoidance of animal products on the premise that the harvesting or industrial farming of animals is environmentally damaging and unsustainable.",
  "Breakfast": "Breakfast is the first meal of a day. The word in English refers to breaking the fasting period of the previous night. There is a strong likelihood for one or more \"typical\", or \"traditional\", breakfast menus to exist in most places, but their composition varies widely from place to place, and has varied over time, so that globally a very wide range of preparations and ingredients are now associated with breakfast.",
}

recipes = {
  "Beef and Mustard Pie": {
    "ingredients": ["1kg Beef", "2 tbs Plain Flour","2 tbs Rapeseed Oil","200ml Red Wine","400ml Beef Stock", "1 finely sliced Onion", "2 chopped Carrots", "3 sprigs Thyme", "2 tbs Mustard", "2 free-range Egg Yolks", "400g Puff Pastry", "300g Green Beans", "25g Butter","pinch Salt", "pinch Pepper"],
    "steps": ["Preheat the oven to 150C/300F/Gas 2.\r\nToss the beef and flour together in a bowl with some salt and black pepper.\r\nHeat a large casserole until hot, add half of the rapeseed oil and enough of the beef to just cover the bottom of the casserole.\r\nFry until browned on each side, then remove and set aside. Repeat with the remaining oil and beef.\r\nReturn the beef to the pan, add the wine and cook until the volume of liquid has reduced by half, then add the stock, onion, carrots, thyme and mustard, and season well with salt and pepper.\r\nCover with a lid and place in the oven for two hours.\r\nRemove from the oven, check the seasoning and set aside to cool. Remove the thyme.\r\nWhen the beef is cool and you're ready to assemble the pie, preheat the oven to 200C/400F/Gas 6.\r\nTransfer the beef to a pie dish, brush the rim with the beaten egg yolks and lay the pastry over the top. Brush the top of the pastry with more beaten egg.\r\nTrim the pastry so there is just enough excess to crimp the edges, then place in the oven and bake for 30 minutes, or until the pastry is golden-brown and cooked through.\r\nFor the green beans, bring a saucepan of salted water to the boil, add the beans and cook for 4-5 minutes, or until just tender.\r\nDrain and toss with the butter, then season with black pepper.\r\nTo serve, place a large spoonful of pie onto each plate with some green beans alongside."]
  },
  "Beef Bourguignon":{
    "ingredients": ['3 tsp Goose Fat', '600g Beef Shin', '100g  Bacon', '350g Challots', '250g Chestnut Mushroom', '2 sliced Garlic Clove', '1 Bouquet Garni', '1 tbs Tomato Puree', '750 ml  Red Wine', '600g Celeriac', '2 tbs Olive Oil', 'sprigs of fresh Thyme', 'sprigs of fresh Rosemary', '2 Bay Leaf', '4 Cardamom'],
    "steps": ["Heat a large casserole pan and add 1 tbsp goose fat. Season the beef and fry until golden brown, about 3-5 mins, then turn over and fry the other side until the meat is browned all over, adding more fat if necessary. Do this in 2-3 batches, transferring the meat to a colander set over a bowl when browned.\r\nIn the same pan, fry the bacon, shallots or pearl onions, mushrooms, garlic and bouquet garni until lightly browned. Mix in the tomato purée and cook for a few mins, stirring into the mixture. This enriches the bourguignon and makes a great base for the stew. Then return the beef and any drained juices to the pan and stir through.\r\nPour over the wine and about 100ml water so the meat bobs up from the liquid, but isn’t completely covered. Bring to the boil and use a spoon to scrape the caramelised cooking juices from the bottom of the pan – this will give the stew more flavour.\r\nHeat oven to 150C/fan 130C/gas 2. Make a cartouche: tear off a square of foil slightly larger than the casserole, arrange it in the pan so it covers the top of the stew and trim away any excess foil. Then cook for 3 hrs. If the sauce looks watery, remove the beef and veg with a slotted spoon, and set aside. Cook the sauce over a high heat for a few mins until the sauce has thickened a little, then return the beef and vegetables to the pan.\r\nTo make the celeriac mash, peel the celeriac and cut into cubes. Heat the olive oil in a large frying pan. Tip in the celeriac and fry for 5 mins until it turns golden. Season well with salt and pepper. Stir in the rosemary, thyme, bay and cardamom pods, then pour over 200ml water, enough to nearly cover the celeriac. Turn the heat to low, partially cover the pan and leave to simmer for 25-30 mins.\r\nAfter 25-30 mins, the celeriac should be soft and most of the water will have evaporated. Drain away any remaining water, then remove the herb sprigs, bay and cardamom pods. Lightly crush with a potato masher, then finish with a glug of olive oil and season to taste. Spoon the beef bourguignon into serving bowls and place a large spoonful of the celeriac mash on top. Garnish with one of the bay leaves, if you like."]
  },
  "Beef Rendang": {
    "ingredients": ['1lb Beef', '5 tbs Vegetable Oil', '1 Cinnamon Stick', '3 Cloves', '3 Star Anise', '3 Cardamom', '1 cup  Coconut Cream', '1 cup  Water', '2 tbs Tamarind Paste', '6 Lime', '1 tbs Sugar', '5 Challots'],
    "steps": ["Chop the spice paste ingredients and then blend it in a food processor until fine.\r\nHeat the oil in a stew pot, add the spice paste, cinnamon, cloves, star anise, and cardamom and stir-fry until aromatic. Add the beef and the pounded lemongrass and stir for 1 minute. Add the coconut milk, tamarind juice, water, and simmer on medium heat, stirring frequently until the meat is almost cooked. Add the kaffir lime leaves, kerisik (toasted coconut), sugar or palm sugar, stirring to blend well with the meat.\r\nLower the heat to low, cover the lid, and simmer for 1 to 1 1/2 hours or until the meat is really tender and the gravy has dried up. Add more salt and sugar to taste. Serve immediately with steamed rice and save some for overnight."]
  },
  "Beef Wellington": {
    "ingredients": ['400g mushrooms', '1-2tbsp English Mustard', 'Dash Olive Oil', '750g piece Beef Fillet', '6-8 slices Parma ham', '500g Puff Pastry', 'Dusting Flour', '2 Beaten  Egg Yolks'],
    "steps": ["Put the mushrooms into a food processor with some seasoning and pulse to a rough paste. Scrape the paste into a pan and cook over a high heat for about 10 mins, tossing frequently, to cook out the moisture from the mushrooms. Spread out on a plate to cool.\r\nHeat in a frying pan and add a little olive oil. Season the beef and sear in the hot pan for 30 secs only on each side. (You don't want to cook it at this stage, just colour it). Remove the beef from the pan and leave to cool, then brush all over with the mustard.\r\nLay a sheet of cling film on a work surface and arrange the Parma ham slices on it, in slightly overlapping rows. With a palette knife, spread the mushroom paste over the ham, then place the seared beef fillet in the middle. Keeping a tight hold of the cling film from the edge, neatly roll the Parma ham and mushrooms around the beef to form a tight barrel shape. Twist the ends of the cling film to secure. Chill for 15-20 mins to allow the beef to set and keep its shape.\r\nRoll out the puff pastry on a floured surface to a large rectangle, the thickness of a £1 coin. Remove the cling film from the beef, then lay in the centre. Brush the surrounding pastry with egg yolk. Fold the ends over, the wrap the pastry around the beef, cutting off any excess. Turn over, so the seam is underneath, and place on a baking sheet. Brush over all the pastry with egg and chill for about 15 mins to let the pastry rest.\r\nHeat the oven to 200C, 400F, gas 6.\r\nLightly score the pastry at 1cm intervals and glaze again with beaten egg yolk. Bake for 20 minutes, then lower the oven setting to 180C, 350F, gas 4 and cook for another 15 mins. Allow to rest for 10-15 mins before slicing and serving with the side dishes of your choice. The beef should still be pink in the centre when you serve it."]
  },
  "Steak and Kidney Pie": {
    "ingredients": ['300g Puff Pastry', 'Beaten Egg White', 'Beaten Egg Yolks', '2 tbs Vegetable Oil', '70 ml  Beef', '200g Lamb Kidney', '2 chopped Onions', '30g Plain Flour', '85 ml  Beef Stock', 'pinch Salt', 'pinch Pepper', 'Dash Worcestershire Sauce'],
    "steps": ["Preheat the oven to 220C/425F/Gas 7\r\nHeat the vegetable oil in a large frying pan, and brown the beef all over. (You may need to do this in batches.) Set aside, then brown the kidneys on both sides in the same pan. Add the onions and cook for 3-4 minutes.\r\nReturn the beef to the pan, sprinkle flour over and coat the meat and onions\r\nAdd the stock to the pan, stir well and bring to the boil.\r\nTurn the heat down and simmer for 1½ hours without a lid. If the liquid evaporates too much, add more stock.\r\nRemove from the heat. Add salt, pepper and Worcestershire sauce and allow to cool completely. Place the cooked meat mixture into a pie dish.\r\nRoll out the pastry to 5mm/¼in thick and 5cm/2in larger than the dish you are using.\r\nUsing a rolling pin, lift the pastry and place it over the top of the pie dish. Trim and crimp the edges with your fingers and thumb.\r\nBrush the surface with the beaten egg mixture and bake for 30-40 minutes until golden-brown and puffed.\r\nServe with creamy mash and steamed vegetables to soak up the gravy."]
  },
  "Brown Stew Chicken": {
    "ingredients": ['1 whole Chicken', '1 chopped Tomato', '2 chopped Onions', '2 chopped Garlic Clove', '1 chopped Red Pepper', '1 chopped Carrots', '1 Lime', '2 tsp Thyme', '1 tsp  Allspice', '2 tbs Soy Sauce', '2 tsp Cornstarch', '2 cups  Coconut Milk', '1 tbs Vegetable Oil'],
    "steps": ["Squeeze lime over chicken and rub well. Drain off excess lime juice.\r\nCombine tomato, scallion, onion, garlic, pepper, thyme, pimento and soy sauce in a large bowl with the chicken pieces. Cover and marinate at least one hour.\r\nHeat oil in a dutch pot or large saucepan. Shake off the seasonings as you remove each piece of chicken from the marinade. Reserve the marinade for sauce.\r\nLightly brown the chicken a few pieces at a time in very hot oil. Place browned chicken pieces on a plate to rest while you brown the remaining pieces.\r\nDrain off excess oil and return the chicken to the pan. Pour the marinade over the chicken and add the carrots. Stir and cook over medium heat for 10 minutes.\r\nMix flour and coconut milk and add to stew, stirring constantly. Turn heat down to minimum and cook another 20 minutes or until tender."]
  },
  "Chicken & mushroom Hotpot": {
    "ingredients": ['50g Butter', '1 chopped Onion', '100g  Mushrooms', '40g Plain Flour', '1 Chicken Stock Cube', 'pinch Nutmeg', 'pinch Mustard Powder', '250g Chicken', '2 Handfuls Sweetcorn', '2 large Potatoes', '1 knob Butter'],
    "steps": ["Heat oven to 200C/180C fan/gas 6. Put the butter in a medium-size saucepan and place over a medium heat. Add the onion and leave to cook for 5 mins, stirring occasionally. Add the mushrooms to the saucepan with the onions.\r\n\r\nOnce the onion and mushrooms are almost cooked, stir in the flour – this will make a thick paste called a roux. If you are using a stock cube, crumble the cube into the roux now and stir well. Put the roux over a low heat and stir continuously for 2 mins – this will cook the flour and stop the sauce from having a floury taste.\r\n\r\nTake the roux off the heat. Slowly add the fresh stock, if using, or pour in 500ml water if you’ve used a stock cube, stirring all the time. Once all the liquid has been added, season with pepper, a pinch of nutmeg and mustard powder. Put the saucepan back onto a medium heat and slowly bring it to the boil, stirring all the time. Once the sauce has thickened, place on a very low heat. Add the cooked chicken and vegetables to the sauce and stir well. Grease a medium-size ovenproof pie dish with a little butter and pour in the chicken and mushroom filling.\r\n\r\nCarefully lay the potatoes on top of the hot-pot filling, overlapping them slightly, almost like a pie top.\r\n\r\nBrush the potatoes with a little melted butter and cook in the oven for about 35 mins. The hot-pot is ready once the potatoes are cooked and golden brown."]
  },
  "Chicken Karaage": {
    "ingredients": ['450 grams Boneless skin Chicken thigh', '1 tablespoon Ginger', '1 clove Garlic', '2 tablespoons Soy sauce', '1 tablespoon Sake', '2 teaspoon Granulated sugar', '1/3 cup Potato starch', '1/3 cup Vegetable oil', '1/3 cup Lemon'],
    "steps": ["Add the ginger, garlic, soy sauce, sake and sugar to a bowl and whisk to combine. Add the chicken, then stir to coat evenly. Cover and refrigerate for at least 1 hour.\r\n\r\nAdd 1 inch of vegetable oil to a heavy bottomed pot and heat until the oil reaches 360 degrees F. Line a wire rack with 2 sheets of paper towels and get your tongs out. Put the potato starch in a bowl\r\n\r\nAdd a handful of chicken to the potato starch and toss to coat each piece evenly.\r\n\r\nFry the karaage in batches until the exterior is a medium brown and the chicken is cooked through. Transfer the fried chicken to the paper towel lined rack. If you want the karaage to stay crispy longer, you can fry the chicken a second time, until it's a darker color after it's cooled off once. Serve with lemon wedges."]
  },
  "French Onion Chicken with Roasted Carrots & Mashed Potatoes": {
    "ingredients": ['2 Chicken Breasts', '12 ounces Carrots', '5 Small Potatoes', '1 Onion', '1 Beef Stock', '1 1/2 cup  Mozzarella', '2 tbsp Sour Cream', '  Butter', '  Sugar', '  Vegetable Oil', '  Salt', '  Pepper'],
    "steps": ["1\r\n\r\nPreheat oven to 425 degrees. Wash and dry all produce. Trim, peel, and cut carrots on a diagonal into ¼-inch-thick pieces. Dice potatoes into ½-inch pieces. Halve, peel, and thinly slice onion.\r\n\r\n2\r\n\r\nToss carrots on a baking sheet with a drizzle of oil, salt, and pepper. Roast until browned and tender, 15-20 minutes.\r\n\r\n3\r\n\r\nMeanwhile, place potatoes in a medium pot with enough salted water to cover by 2 inches. Bring to a boil and cook until tender, 12-15 minutes. Drain and return potatoes to pot; cover to keep warm.\r\n\r\n4\r\n\r\nWhile potatoes cook, heat a drizzle of oil in a large pan over medium-high heat. Add onion and cook, stirring occasionally, until lightly browned and softened, 8-10 minutes. Sprinkle with 1 tsp sugar (2 tsp for 4 servings). Stir in stock concentrate and 2 TBSP water (¼ cup for 4); season with salt and pepper. Cook until jammy, 2-3 minutes more. Turn off heat; transfer to a small bowl. Wash out pan.\r\n\r\n5\r\n\r\nPat chicken dry with paper towels; season all over with salt and pepper. Heat a drizzle of oil in pan used for onion over medium-high heat. Add chicken and cook until browned and cooked through, 5-6 minutes per side. In the last 1-2 minutes of cooking, top with caramelized onion and cheese. Cover pan until cheese melts. (If your pan doesn’t have a lid, cover with a baking sheet!)\r\n\r\n6\r\n\r\nHeat pot with drained potatoes over low heat; mash with sour cream, 2 TBSP butter (4 TBSP for 4 servings), salt, pepper, and a splash of water (or milk, for extra richness) until smooth. Divide chicken, roasted carrots, and mashed potatoes between plates."]
  },
  "Teriyaki Chicken Casserole": {
    "ingredients": ['3/4 cup soy sauce', '1/2 cup water', '1/4 cup brown sugar', '1/2 teaspoon ground ginger', '1/2 teaspoon minced garlic', '4 Tablespoons cornstarch', '2 chicken breasts', '1 (12 oz.) stir-fry vegetables', '3 cups brown rice'],
    "steps": ["Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!"]
  },
  "Apple & Blackberry Crumbl": {
    "ingredients": ['120g Plain Flour', '60g Caster Sugar', '60g Butter', '300g Braeburn Apples', '30g Butter', '30g Demerara Sugar', '120g Blackberrys', '¼ teaspoon Cinnamon', 'to serve Ice Cream'],
    "steps": ["Heat oven to 190C/170C fan/gas 5. Tip the flour and sugar into a large bowl. Add the butter, then rub into the flour using your fingertips to make a light breadcrumb texture. Do not overwork it or the crumble will become heavy. Sprinkle the mixture evenly over a baking sheet and bake for 15 mins or until lightly coloured.\r\nMeanwhile, for the compote, peel, core and cut the apples into 2cm dice. Put the butter and sugar in a medium saucepan and melt together over a medium heat. Cook for 3 mins until the mixture turns to a light caramel. Stir in the apples and cook for 3 mins. Add the blackberries and cinnamon, and cook for 3 mins more. Cover, remove from the heat, then leave for 2-3 mins to continue cooking in the warmth of the pan.\r\nTo serve, spoon the warm fruit into an ovenproof gratin dish, top with the crumble mix, then reheat in the oven for 5-10 mins. Serve with vanilla ice cream."]
  },
  "Banana Pancakes": {
    "ingredients": ['1 large Banana', '2 medium Eggs', 'pinch Baking Powder', 'spinkling Vanilla Extract', '1 tsp  Oil', '25g Pecan Nuts', '125g Raspberries'],
    "steps": ["In a bowl, mash the banana with a fork until it resembles a thick purée. Stir in the eggs, baking powder and vanilla.\r\nHeat a large non-stick frying pan or pancake pan over a medium heat and brush with half the oil. Using half the batter, spoon two pancakes into the pan, cook for 1-2 mins each side, then tip onto a plate. Repeat the process with the remaining oil and batter. Top the pancakes with the pecans and raspberries."]
  },
  "Bread and Butter Pudding": {
    "ingredients": ['25g/1oz butter', '8 thin slices bread', '50g/2oz sultanas', '2 tsp cinnamon', '350ml/12fl milk', '50ml/2fl oz double cream', '2 free-range eggs', '25g/1oz sugar', 'grated, to taste nutmeg'],
    "steps": ["Grease a 1 litre/2 pint pie dish with butter.\r\nCut the crusts off the bread. Spread each slice with on one side with butter, then cut into triangles.\r\nArrange a layer of bread, buttered-side up, in the bottom of the dish, then add a layer of sultanas. Sprinkle with a little cinnamon, then repeat the layers of bread and sultanas, sprinkling with cinnamon, until you have used up all of the bread. Finish with a layer of bread, then set aside.\r\nGently warm the milk and cream in a pan over a low heat to scalding point. Don't let it boil.\r\nCrack the eggs into a bowl, add three quarters of the sugar and lightly whisk until pale.\r\nAdd the warm milk and cream mixture and stir well, then strain the custard into a bowl.\r\nPour the custard over the prepared bread layers and sprinkle with nutmeg and the remaining sugar and leave to stand for 30 minutes.\r\nPreheat the oven to 180C/355F/Gas 4.\r\nPlace the dish into the oven and bake for 30-40 minutes, or until the custard has set and the top is golden-brown."]
  },
  "Carrot Cake": {
    "ingredients": ['450ml Vegetable Oil', '400g Plain Flour', '2 tsp Bicarbonate Of Soda', '550ml Sugar', '5 Eggs', '½ tsp Salt', '2 tsp Cinnamon', '500g grated Carrots', '150g Walnuts', '200g Cream Cheese', '150g Caster Sugar', '100g  Butter'],
    "steps": ["For the carrot cake, preheat the oven to 160C/325F/Gas 3. Grease and line a 26cm/10in springform cake tin.\r\nMix all of the ingredients for the carrot cake, except the carrots and walnuts, together in a bowl until well combined. Stir in the carrots and walnuts.\r\nSpoon the mixture into the cake tin and bake for 1 hour 15 minutes, or until a skewer inserted into the middle comes out clean. Remove the cake from the oven and set aside to cool for 10 minutes, then carefully remove the cake from the tin and set aside to cool completely on a cooling rack.\r\nMeanwhile, for the icing, beat the cream cheese, caster sugar and butter together in a bowl until fluffy. Spread the icing over the top of the cake with a palette knife."]
  },
  "Chocolate Raspberry Brownies": {
    "ingredients": ['200g Dark Chocolate', '100g  Milk Chocolate', '250g Salted Butter', '400g Light Brown Soft Sugar', '4 large Eggs', '140g Plain Flour', '50g Cocoa', '200g Raspberries],
    "steps": ["Heat oven to 180C/160C fan/gas 4. Line a 20 x 30cm baking tray tin with baking parchment. Put the chocolate, butter and sugar in a pan and gently melt, stirring occasionally with a wooden spoon. Remove from the heat.\r\nStir the eggs, one by one, into the melted chocolate mixture. Sieve over the flour and cocoa, and stir in. Stir in half the raspberries, scrape into the tray, then scatter over the remaining raspberries. Bake on the middle shelf for 30 mins or, if you prefer a firmer texture, for 5 mins more. Cool before slicing into squares. Store in an airtight container for up to 3 days."]
  },
  "Lamb and Lemon Souvlaki": {
    "ingredients": ['2 cloves Garlic', '2 tsp Sea Salt', '4 tbs Olive Oil', 'Zest and juice of 1 Lemon', '1 tbs Dill', '750g Lamb Leg', 'To serve Pita Bread'],
    "steps": ["Pound the garlic with sea salt in a pestle and mortar (or use a small food processor), until the garlic forms a paste. Whisk together the oil, lemon juice, zest, dill and garlic. Mix in the lamb and combine well. Cover and marinate for at least 2 hrs or overnight in the fridge. If you\u2019re going to use bamboo skewers, soak them in cold water.\r\n\r\nIf you\u2019ve prepared the lamb the previous day, take it out of the fridge 30 mins before cooking. Thread the meat onto the soaked or metal skewers. Heat the grill to high or have a hot griddle pan or barbecue ready. Cook the skewers for 2-3 mins on each side, basting with the remaining marinade. Heat the pitta or flatbreads briefly, then stuff with the souvlaki. Add Greek salad (see 'Goes well with', right) and Tzatziki (below), if you like."]
  },
  "Bean & Sausage Hotpot": {
    "ingredients": ['8 large Sausages', '1 Jar Tomato Sauce', '1200g Butter Beans', '1 tbls Black Treacle', '1 tsp  English Mustard'],
    "steps": ["In a large casserole, fry the sausages until brown all over \u2013 about 10 mins.\r\n\r\nAdd the tomato sauce, stirring well, then stir in the beans, treacle or sugar and mustard. Bring to the simmer, cover and cook for 30 mins. Great served with crusty bread or rice."]
  },
  "French Lentils With Garlic and Thyme": {
    "ingredients": ['3 tablespoons Olive Oil', '1 Onion', '2 cloves Garlic', '1 Carrot', '2 1\\/4 cups French Lentils', '1 teaspoon Thyme', '3 Bay Leaf', '1 tablespoon Salt', '2 sticks Celery'],
    "steps": ["Place a large saucepan over medium heat and add oil. When hot, add chopped vegetables and saut\u00e9 until softened, 5 to 10 minutes.\r\nAdd 6 cups water, lentils, thyme, bay leaves and salt. Bring to a boil, then reduce to a fast simmer.\r\nSimmer lentils until they are tender and have absorbed most of the water, 20 to 25 minutes. If necessary, drain any excess water after lentils have cooked. Serve immediately, or allow them to cool and reheat later.\r\nFor a fuller taste, use some chicken stock and reduce the water by the same amount."]
  },
  "Pizza Express Margherita": {
    "ingredients": ['150ml Water', '1 tsp  Sugar', '15g Yeast', '225g Plain Flour', '1 1\\/2 tsp  Salt', 'Drizzle Olive Oil', '80g Passata', '70g Mozzarella', 'Peeled and Sliced Oregano', 'Leaves Basil', 'Pinch Black Pepper'],
    "steps": ["1 Preheat the oven to 230\u00b0C.\r\n\r\n2 Add the sugar and crumble the fresh yeast into warm water.\r\n\r\n3 Allow the mixture to stand for 10 \u2013 15 minutes in a warm place (we find a windowsill on a sunny day works best) until froth develops on the surface.\r\n\r\n4 Sift the flour and salt into a large mixing bowl, make a well in the middle and pour in the yeast mixture and olive oil.\r\n\r\n5 Lightly flour your hands, and slowly mix the ingredients together until they bind.\r\n\r\n6 Generously dust your surface with flour.\r\n\r\n7 Throw down the dough and begin kneading for 10 minutes until smooth, silky and soft.\r\n\r\n8 Place in a lightly oiled, non-stick baking tray (we use a round one, but any shape will do!)\r\n\r\n9 Spread the passata on top making sure you go to the edge.\r\n\r\n10 Evenly place the mozzarella (or other cheese) on top, season with the oregano and black pepper, then drizzle with a little olive oil.\r\n\r\n11 Cook in the oven for 10 \u2013 12 minutes until the cheese slightly colours.\r\n\r\n12 When ready, place the basil leaf on top and tuck in!"]
  },
  "Poutine": {
    "ingredients": ['Dash Vegetable Oil', '1 Can Beef Gravy', '5 thin cut Potatoes', '2 cups Cheese Curds'],
    "steps": ["Heat oil in a deep fryer or deep heavy skillet to 365\u00b0F (185\u00b0C).\r\nWarm gravy in saucepan or microwave.\r\nPlace the fries into the hot oil, and cook until light brown, about 5 minutes.\r\nRemove to a paper towel lined plate to drain.\r\nPlace the fries on a serving platter, and sprinkle the cheese over them.\r\nLadle gravy over the fries and cheese, and serve immediately."]
  },
  "Spaghetti alla Carbonara": {
    "ingredients": ['320g Spaghetti', '6 Egg Yolks', 'As required Salt', '150g Bacon', '50g Pecorino', 'As required Black Pepper'],
    "steps": ["STEP 1\r\nPut a large saucepan of water on to boil.\r\n\r\nSTEP 2\r\nFinely chop the 100g pancetta, having first removed any rind. Finely grate 50g pecorino cheese and 50g parmesan and mix them together.\r\n\r\nSTEP 3\r\nBeat the 3 large eggs in a medium bowl and season with a little freshly grated black pepper. Set everything aside.\r\n\r\nSTEP 4\r\nAdd 1 tsp salt to the boiling water, add 350g spaghetti and when the water comes back to the boil, cook at a constant simmer, covered, for 10 minutes or until al dente (just cooked).\r\n\r\nSTEP 5\r\nSquash 2 peeled plump garlic cloves with the blade of a knife, just to bruise it.\r\n\r\nSTEP 6\r\nWhile the spaghetti is cooking, fry the pancetta with the garlic. Drop 50g unsalted butter into a large frying pan or wok and, as soon as the butter has melted, tip in the pancetta and garlic.\r\n\r\nSTEP 7\r\nLeave to cook on a medium heat for about 5 minutes, stirring often, until the pancetta is golden and crisp. The garlic has now imparted its flavour, so take it out with a slotted spoon and discard.\r\n\r\nSTEP 8\r\nKeep the heat under the pancetta on low. When the pasta is ready, lift it from the water with a pasta fork or tongs and put it in the frying pan with the pancetta. Don\u2019t worry if a little water drops in the pan as well (you want this to happen) and don\u2019t throw the pasta water away yet.\r\n\r\nSTEP 9\r\nMix most of the cheese in with the eggs, keeping a small handful back for sprinkling over later.\r\n\r\nSTEP 10\r\nTake the pan of spaghetti and pancetta off the heat. Now quickly pour in the eggs and cheese. Using the tongs or a long fork, lift up the spaghetti so it mixes easily with the egg mixture, which thickens but doesn\u2019t scramble, and everything is coated.\r\n\r\nSTEP 11\r\nAdd extra pasta cooking water to keep it saucy (several tablespoons should do it). You don\u2019t want it wet, just moist. Season with a little salt, if needed.\r\n\r\nSTEP 12\r\nUse a long-pronged fork to twist the pasta on to the serving plate or bowl. Serve immediately with a little sprinkling of the remaining cheese and a grating of black pepper. If the dish does get a little dry before serving, splash in some more hot pasta water and the glossy sauciness will be revived."]
  },
  "BBQ Pork Sloppy Joes": {
    "ingredients": ['2 Potatoes', '1 Red Onions', '2 cloves Garlic', '1 Lime', '2 Bread', '1 lb Pork', '  Barbeque Sauce', '  Hotsauce', '  Tomato Ketchup', '  Sugar', '  Vegetable Oil', '  Salt', '  Pepper'],
    "steps": ["1\r\n\r\nPreheat oven to 450 degrees. Wash and dry all produce. Cut sweet potatoes into \u00bd-inch-thick wedges. Toss on a baking sheet with a drizzle of oil, salt, and pepper. Roast until browned and tender, 20-25 minutes.\r\n\r\n2\r\n\r\nMeanwhile, halve and peel onion. Slice as thinly as possible until you have \u00bc cup (\u00bd cup for 4 servings); finely chop remaining onion. Peel and finely chop garlic. Halve lime; squeeze juice into a small bowl. Halve buns. Add 1 TBSP butter (2 TBSP for 4) to a separate small microwave-safe bowl; microwave until melted, 30 seconds. Brush onto cut sides of buns.\r\n\r\n3\r\n\r\nTo bowl with lime juice, add sliced onion, \u00bc tsp sugar (\u00bd tsp for 4 servings), and a pinch of salt. Stir to combine; set aside to quick-pickle.\r\n\r\n4\r\n\r\nHeat a drizzle of oil in a large pan over medium-high heat. Add chopped onion and season with salt and pepper. Cook, stirring, until softened, 4-5 minutes. Add garlic and cook until fragrant, 30 seconds more. Add pork and season with salt and pepper. Cook, breaking up meat into pieces, until browned and cooked through, 4-6 minutes.\r\n\r\n5\r\n\r\nWhile pork cooks, in a third small bowl, combine BBQ sauce, pickling liquid from onion, 3 TBSP ketchup (6 TBSP for 4 servings), \u00bd tsp sugar (1 tsp for 4), and \u00bc cup water (\u2153 cup for 4). Once pork is cooked through, add BBQ sauce mixture to pan. Cook, stirring, until sauce is thickened, 2-3 minutes. Taste and season with salt and pepper.\r\n\r\n6\r\n\r\nMeanwhile, toast buns in oven or toaster oven until golden, 3-5 minutes. Divide toasted buns between plates and fill with as much BBQ pork as you\u2019d like. Top with pickled onion and hot sauce. Serve with sweet potato wedges on the side."]
  },
  "Baked salmon with fennel & tomatoes": {
    "ingredients": ['2 medium Fennel', '2 tbs chopped Parsley', 'Juice of 1 Lemon', '175g Cherry Tomatoes', '1 tbs Olive Oil', '350g Salmon', 'to serve Black Olives'],
    "steps": ["Heat oven to 180C\/fan 160C\/gas 4. Trim the fronds from the fennel and set aside. Cut the fennel bulbs in half, then cut each half into 3 wedges. Cook in boiling salted water for 10 mins, then drain well. Chop the fennel fronds roughly, then mix with the parsley and lemon zest.\r\n\r\nSpread the drained fennel over a shallow ovenproof dish, then add the tomatoes. Drizzle with olive oil, then bake for 10 mins. Nestle the salmon among the veg, sprinkle with lemon juice, then bake 15 mins more until the fish is just cooked. Scatter over the parsley and serve."]
  },
  "Cajun spiced fish tacos": {
    "ingredients": ['2 tbsp cajun', '1 tsp cayenne pepper', '4 fillets white fish', '1 tsp vegetable oil', '8 flour tortilla', '1 sliced avocado', '2 shredded little gem lettuce', '4 shredded spring onion', '1 x 300ml salsa', '1 pot sour cream', '1 lemon', '1 clove finely chopped garlic'],
    "steps": ["Cooking in a cajun spice and cayenne pepper marinade makes this fish super succulent and flavoursome. Top with a zesty dressing and serve in a tortilla for a quick, fuss-free main that's delightfully summery.\r\n\r\nOn a large plate, mix the cajun spice and cayenne pepper with a little seasoning and use to coat the fish all over.\r\n\r\nHeat a little oil in a frying pan, add in the fish and cook over a medium heat until golden. Reduce the heat and continue frying until the fish is cooked through, about 10 minutes. Cook in batches if you don\u2019t have enough room in the pan.\r\n\r\nMeanwhile, prepare the dressing by combining all the ingredients with a little seasoning.\r\nSoften the tortillas by heating in the microwave for 5-10 seconds. Pile high with the avocado, lettuce and spring onion, add a spoonful of salsa, top with large flakes of fish and drizzle over the dressing."]
  },
  "Fish pie": {
    "ingredients": ['900g Floury Potatoes', '2 tbsp Olive Oil', '600ml Semi-skimmed Milk', '800g White Fish Fillets', '1 tbsp Plain flour', 'Grating Nutmeg', '3 tbsp Double Cream', '200g Jerusalem Artichokes', '1 finely sliced Leek', '200g peeled raw Prawns', 'Large handful Parsley', 'Handful Dill', 'Grated zest of 1 Lemon', '25g grated Gruyère', 'Juice of 1 Lemon'],
    "steps": ["01.Put the potatoes in a large pan of cold salted water and bring to the boil. Lower the heat, cover, then simmer gently for 15 minutes until tender. Drain, then return to the pan over a low heat for 30 seconds to drive off any excess water. Mash with 1 tbsp olive oil, then season.\r\n02.Meanwhile put the milk in a large saut\u00e9 pan, add the fish and bring to the boil. Remove from the heat, cover and stand for 3 minutes. Remove the fish (reserving the milk) and pat dry with kitchen paper, then gently flake into an ovenproof dish, discarding the skin and any bones.\r\n03.Heat the remaining oil in a pan, stir in the flour and cook for 30 seconds. Gradually stir in 200-250ml of the reserved milk (discard the rest). Grate in nutmeg, season, then bubble until thick. Stir in the cream.\r\n04.Preheat the oven to 190\u00b0C\/fan170\u00b0C\/gas 5. Grate the artichokes and add to the dish with the leek, prawns and herbs. Stir the lemon zest and juice into the sauce, then pour over. Mix gently with a wooden spoon.\r\n05.Spoon the mash onto the fish mixture, then use a fork to make peaks, which will crisp and brown as it cooks. Sprinkle over the cheese, then bake for 35-40 minutes until golden and bubbling. Serve with wilted greens."]
  },
  "Honey Teriyaki Salmon": {
    "ingredients": ['1 lb Salmon', '1 tablespoon Olive oil', '2 tablespoons Soy Sauce', '2 tablespoons Sake', '4 tablespoons Sesame Seed'],
    "steps": ["Mix all the ingredients in the Honey Teriyaki Glaze together. Whisk to blend well. Combine the salmon and the Glaze together.\r\n\r\nHeat up a skillet on medium-low heat. Add the oil, Pan-fry the salmon on both sides until it’s completely cooked inside and the glaze thickens.\r\n\r\nGarnish with sesame and serve immediately."]
  },
  "Kung Po Prawn": {
    "ingredients": ['400g Prawns', '2 tbs Soy Sauce', '1 tsp  Tomato Puree', '1 tsp  Corn Flour', '1 tsp  Caster Sugar', '1 tsp  Sunflower Oil', '85g Peanuts', '3 Large Chilli', '1 tbs Brown Sugar', '6 cloves Garlic Clove', '450g Water Chestnut', 'to taste Ginger'],
    "steps": ["Mix the cornflour and 1 tbsp soy sauce, toss in the prawns and set aside for 10 mins. Stir the vinegar, remaining soy sauce, tomato pur\u00e9e, sugar and 2 tbsp water together to make a sauce.\r\n\r\nWhen you\u2019re ready to cook, heat a large frying pan or wok until very hot, then add 1 tbsp oil. Fry the prawns until they are golden in places and have opened out\u2013 then tip them out of the pan.\r\n\r\nHeat the remaining oil and add the peanuts, chillies and water chestnuts. Stir-fry for 2 mins or until the peanuts start to colour, then add the ginger and garlic and fry for 1 more min. Tip in the prawns and sauce and simmer for 2 mins until thickened slightly. Serve with rice."]
  },
  "Boulangère Potatoe": {
    "ingredients": ['2 finely chopped Onions', 'sprigs of fresh Thyme', '2 tbs Olive Oil', '1.5kg Potatoes', '425g Vegetable Stock'],
    "steps": ["Heat oven to 200C\/fan 180C\/gas 6. Fry the onions and thyme sprigs in the oil until softened and lightly coloured (about 5 mins).\r\nSpread a layer of potatoes over the base of a 1.5-litre oiled gratin dish. Sprinkle over a few onions (see picture, above) and continue layering, finishing with a layer of potatoes. Pour over the stock and bake for 50-60 mins until the potatoes are cooked and the top is golden and crisp."]
  },
  "Cream Cheese Tart": {
    "ingredients": ['250g Flour', '125g Butter', '1 Egg', 'Pinch Salt', '300g Cheese', '100ml milk Milk', '3 Eggs', '100g Parmesan Cheese', '350g Plum tomatoes', '3tbsp White Vinegar', '1 tbsp Honey', 'Topping Basil'],
    "steps": ["Crust: make a dough from 250g flour (I like mixing different flours like plain and wholegrain spelt flour), 125g butter, 1 egg and a pinch of salt, press it into a tart form and place it in the fridge. Filling: stir 300g cream cheese and 100ml milk until smooth, add in 3 eggs, 100g grated parmesan cheese and season with salt, pepper and nutmeg. Take the crust out of the fridge and prick the bottom with a fork. Pour in the filling and bake at 175 degrees C for about 25 minutes. Cover the tart with some aluminium foil after half the time. In the mean time, slice about 350g mini tomatoes. In a small pan heat 3tbsp olive oil, 3tbsp white vinegar, 1 tbsp honey, salt and pepper and combine well. Pour over the tomato slices and mix well. With a spoon, place the tomato slices on the tart, avoiding too much liquid on it. Decorate with basil leaves and enjoy"]
  },
  "Broccoli & Stilton soup": {
    "ingredients": ['2 tblsp  Rapeseed Oil', '1 finely chopped  Onion', '1 Celery', '1 sliced Leek', '1 medium Potatoes', '1 knob Butter', '1 litre hot Vegetable Stock', '1 Head chopped Broccoli', '140g Stilton Cheese'],
    "steps": ["Heat the rapeseed oil in a large saucepan and then add the onions. Cook on a medium heat until soft. Add a splash of water if the onions start to catch.\r\n\r\nAdd the celery, leek, potato and a knob of butter. Stir until melted, then cover with a lid. Allow to sweat for 5 minutes. Remove the lid.\r\n\r\nPour in the stock and add any chunky bits of broccoli stalk. Cook for 10 \u2013 15 minutes until all the vegetables are soft.\r\n\r\nAdd the rest of the broccoli and cook for a further 5 minutes. Carefully transfer to a blender and blitz until smooth. Stir in the stilton, allowing a few lumps to remain. Season with black pepper and serve."]
  },
  "Breakfast Potatoes": {
    "ingredients": ['3 Medium Potatoes', '1 tbs Olive Oil', '2 strips Bacon', 'Minced Garlic Clove', '1 tbs Maple Syrup', 'Garnish Parsley', 'Pinch Salt', 'Pinch Pepper', 'To taste Allspice'],
    "steps": ["Before you do anything, freeze your bacon slices that way when you're ready to prep, it'll be so much easier to chop!\r\nWash the potatoes and cut medium dice into square pieces. To prevent any browning, place the already cut potatoes in a bowl filled with water.\r\nIn the meantime, heat 1-2 tablespoons of oil in a large skillet over medium-high heat. Tilt the skillet so the oil spreads evenly.\r\nOnce the oil is hot, drain the potatoes and add to the skillet. Season with salt, pepper, and Old Bay as needed.\r\nCook for 10 minutes, stirring the potatoes often, until brown. If needed, add a tablespoon more of oil.\r\nChop up the bacon and add to the potatoes. The bacon will start to render and the fat will begin to further cook the potatoes. Toss it up a bit! The bacon will take 5-6 minutes to crisp.\r\nOnce the bacon is cooked, reduce the heat to medium-low, add the minced garlic and toss. Season once more. Add dried or fresh parsley. Control heat as needed.\r\nLet the garlic cook until fragrant, about one minute.\r\nJust before serving, drizzle over the maple syrup and toss. Let that cook another minute, giving the potatoes a caramelized effect.\r\nServe in a warm bowl with a sunny side up egg!"]
  },
  "Full English Breakfast": {
    "ingredients": ['4 Sausages', '4 Bacon', '4 Mushrooms', '3 Tomatoes', '2 sliced Black Pudding', '2 Eggs', '1 Slice Bread', '100g  Baked Beans'],
    "steps": ["Heat the flat grill plate over a low heat, on top of 2 rings\/flames if it fits, and brush sparingly with light olive oil.\r\nCook the sausages first. Add the sausages to the hot grill plate\/the coolest part if there is one and allow to cook slowly for about 15-20 minutes, turning occasionally, until golden. After the first 10 minutes, increase the heat to medium before beginning to cook the other ingredients. If you are struggling for space, completely cook the sausages and keep hot on a plate in the oven.\r\nSnip a few small cuts into the fatty edge of the bacon. Place the bacon straight on to the grill plate and fry for 2-4 minutes each side or until your preferred crispiness is reached. Like the sausages, the cooked bacon can be kept hot on a plate in the oven.\r\nFor the mushrooms, brush away any dirt using a pastry brush and trim the stalk level with the mushroom top. Season with salt and pepper and drizzle over a little olive oil. Place stalk-side up on the grill plate and cook for 1-2 minutes before turning and cooking for a further 3-4 minutes. Avoid moving the mushrooms too much while cooking, as this releases the natural juices, making them soggy.\r\nFor the tomatoes, cut the tomatoes across the centre\/or in half lengthways if using plum tomatoes , and with a small, sharp knife remove the green 'eye'. Season with salt and pepper and drizzle with a little olive oil. Place cut-side down on the grill plate and cook without moving for 2 minutes. Gently turn over and season again. Cook for a further 2-3 minutes until tender but still holding their shape.\r\nFor the black pudding, cut the black pudding into 3-4 slices and remove the skin. Place on the grill plate and cook for 1\u00bd-2 minutes each side until slightly crispy.\r\nFor 'proper' fried bread it's best to cook it in a separate pan. Ideally, use bread that is a couple of days old. Heat a frying pan to a medium heat and cover the base with oil. Add the bread and cook for 2-3 minutes each side until crispy and golden. If the pan becomes too dry, add a little more oil. For a richer flavour, add a knob of butter after you turn the slice.\r\nFor the fried eggs, break the egg straight into the pan with the fried bread and leave for 30 seconds. Add a good knob of butter and lightly splash\/baste the egg with the butter when melted. Cook to your preferred stage, season and gent]
  },
  "Salmon Eggs Eggs Benedict": {
    "ingredients": ['4 Eggs', '2 tbs White Wine Vinegar', '2 English Muffins', 'To serve Butter', '8 slices Smoked Salmon', '2 tsp Lemon Juice', '2 tsp White Wine Vinegar', '3 Yolkes Egg', '125g Unsalted Butter'],
    "steps": ["First make the Hollandaise sauce. Put the lemon juice and vinegar in a small bowl, add the egg yolks and whisk with a balloon whisk until light and frothy. Place the bowl over a pan of simmering water and whisk until mixture thickens. Gradually add the butter, whisking constantly until thick \u2013 if it looks like it might be splitting, then whisk off the heat for a few mins. Season and keep warm.\r\n\r\nTo poach the eggs, bring a large pan of water to the boil and add the vinegar. Lower the heat so that the water is simmering gently. Stir the water so you have a slight whirlpool, then slide in the eggs one by one. Cook each for about 4 mins, then remove with a slotted spoon.\r\n\r\nLightly toast and butter the muffins, then put a couple of slices of salmon on each half. Top each with an egg, spoon over some Hollandaise and garnish with chopped chives."]
  },

}

# list main inggredients => mainInggredients = recipes.keys()
print("""
#--------------------------------------------------


.-. . .-..----..-.    .---.  .----. .-.   .-..----.
| |/ \| || {_  | |   /  ___}/  {}  \|  `.'  || {_  
|  .'.  || {__ | `--.\     }\      /| |\ /| || {__ 
`-'   `-'`----'`----' `---'  `----' `-' ` `-'`----'
    

#--------------------------------------------------
""")
# question prompt
print("""
# --------------------------------------------------------------



  _____           _                   _______              _     
 |  __ \         (_)                 |__   __|            | |    
 | |__) |___  ___ _ _ __   ___  ___     | | ___  _ __ ___ | |__  
 |  _  // _ \/ __| | '_ \ / _ \/ __|    | |/ _ \| '_ ` _ \| '_ \ 
 | | \ \  __/ (__| | |_) |  __/\__ \    | | (_) | | | | | | |_) |
 |_|  \_\___|\___|_| .__/ \___||___/    |_|\___/|_| |_| |_|_.__/ 
                   | |                                           
                   |_|                                           

# --------------------------------------------------------------
# """)
# print("Welcome to Recipes Tome, what do you want to cook?")
# likes_snakes = input("Do you like snakes? ")
# isVegan = input("Are yu vegan?")
# if likes_snakes:
#   print("Iwwww....")
#   meat = input("Do you like meat? ")
#   if meat:
#     typeMeat = input("Which ones?")
#     if typeMeat == "chicken":
#       print("chicken")
# else:
#   print("That's good")
# print(categories)

# request api
# api_url = "https://www.themealdb.com/api/json/v1/1/categories.php"
# response = requests.get(api_url)
# print(response.json())

# print(isSeeAllCategories)
def showALlCategories():
  for category in categories:
    print(category)
  print("Type the category of your choice to see the menu list. \n:")

def showRecipes(name):
  # print(name)
  myRecipe = recipes[name]
  # print(myRecipe)
  myInggredient = myRecipe["ingredients"]
  myStep = myRecipe["steps"][0].split("\r\n")
  # print(myStep)

  for ingg in myInggredient:
    print(ingg)

  for step in myStep:
    print("- {}".format(step))

def browseRecipes():
  pickedCategory = input()

  if pickedCategory in categories.keys():
    print(descriptions[pickedCategory])

    userCategory = categories[pickedCategory]

    print("We have {} recipe in the list!".format(len(userCategory)))
    print("Good! We will show you the list!")
    for idx, menu in enumerate(userCategory):
      print("{no}. {menu}".format(no=idx, menu=menu))
    
    print("Pick the menu by typing the menu number!\n:")

    chosenRecipeIdx = input()
    if chosenRecipeIdx < len(userCategory):
      chosenRecipeName = userCategory[int(chosenRecipeIdx)]
      print("Here the recipes for {}:".format(chosenRecipeName))
      # show the recipes
      showRecipes(chosenRecipeName)
    else:
      print("You input wrong number!")
      wait()
    
  else:
    print("We don't have {} category in our library!".format(pickedCategory))
    wait()

# ==============START==============

def start():
  isSeeAllCategories = input("Do you want to see all the categories? (Y/N)\n:")
  if isSeeAllCategories == "Y":
    showALlCategories()
    browseRecipes()
  else:
    print("Thank you for you visit! See you later!")
    print("""
# --------------------------------------------------------------
  _____           _                   _______              _     
 |  __ \         (_)                 |__   __|            | |    
 | |__) |___  ___ _ _ __   ___  ___     | | ___  _ __ ___ | |__  
 |  _  // _ \/ __| | '_ \ / _ \/ __|    | |/ _ \| '_ ` _ \| '_ \ 
 | | \ \  __/ (__| | |_) |  __/\__ \    | | (_) | | | | | | |_) |
 |_|  \_\___|\___|_| .__/ \___||___/    |_|\___/|_| |_| |_|_.__/ 
                   | |                                           
                   |_|                                           
# --------------------------------------------------------------
# """)

def wait():
  print("DOu you want to browse our recipes more? (Y/N)\n:")
  isSeeMoreRecipes = input()
  if isSeeMoreRecipes == "Y":
    return True 
  else:
    return False


print("Welcome welcome!!")
print("You can choose recipe from our huge recipes library!")

isStarted = False
while isStarted:
  start()
  isDone = wait()
  isStarted = isDone

# print(isStarted)
if not isStarted:
  print("Thank you for you visit! See you later!")
  print("""
# --------------------------------------------------------------
  _____           _                   _______              _     
 |  __ \         (_)                 |__   __|            | |    
 | |__) |___  ___ _ _ __   ___  ___     | | ___  _ __ ___ | |__  
 |  _  // _ \/ __| | '_ \ / _ \/ __|    | |/ _ \| '_ ` _ \| '_ \ 
 | | \ \  __/ (__| | |_) |  __/\__ \    | | (_) | | | | | | |_) |
 |_|  \_\___|\___|_| .__/ \___||___/    |_|\___/|_| |_| |_|_.__/ 
                   | |                                           
                   |_|                                           
# --------------------------------------------------------------
# """)

