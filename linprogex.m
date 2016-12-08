% solves the linear programming problem
% min c_i * x_i where c_i is the cost of food i, x_i is fraction of 100 g food i
% subject to 600 <= 69x_1 + 18x_2 + 94x_3 >= 2000 ... etc

clear;

% objective function, minimizes total cost of food (prices for tomatoes, potatoes, corn $ / 100g)
food = {'Potatoes', 'Tomatoes', 'Corn'};
nutrients = {'Calories', 'Protein', 'Fat', 'Carbohydrates'};

f = [ 0.06393398; 0.330693; 0.2433906 ];
A = -[ 69 18 94; 1.68 0.88 2.35; 0.1 0.2 0; 15.71 3.89 20 ]; % nutrient constraints for each food
b = -[666.667; 16.667; 21.667; 100]; % b

lb  = [ 0; 0; 0]; % each variable needs to be positive
ub  = [ 10; 10; 10]; % no more than 1000 g

% use linprog to solve the linear programming problem
[x,fval,exitflag,output,lambda]  = linprog(f,A,b,[],[],lb);


% plot the feasible region, contours of the objective, and the optimal solution
x1plot = linspace(0,5,6);
x2plot = linspace(-2,8,11);
figure(); hold on;
plot(x1plot,1+x1plot,'-k','LineWidth',3)
plot(x1plot,2*x1plot-2,'-k','LineWidth',3)
fill([0 0 3 1],[0 1 4 0],'g')
alpha 0.5
plot( x(1), x(2), 'r.','MarkerSize',32)
[X1,X2] = meshgrid(x1plot,x2plot);
contour(X1,X2,X1+X2,24,'-b')