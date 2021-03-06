#populate bank of problems to avoid calling makebank.py
def quickbank():
    """return a fixed problem file as a dictionary"""

        #no parameters
    bank = {'exponents': ['\\item $15x^{2}y^2 \\div 3x^5 y^{2}$\n',
  '\\item $\\sqrt[3]{x^{-9} y^{6}}$\n',
  '\\item $\\displaystyle \\left( x y^{\\frac{1}{4}}\\right)^2$\n'],
 'function-inverse': ['\\item Given $f(x)=x^2+4$ find $f^{-1}(x)$\n',
  '\\item Given $g(x)=x^2-3$ find $g^{-1}(x)$\n',
  '\\item Given $f(x)=\\sqrt{x}+1$ find $f^{-1}(x)$\n',
  '\\item Given $f(x)=x^2-5$ find $f^{-1}(x)$\n'],
 'g-quad-vertex': ['\\item Let $f$ be a quadratic function. Part of the graph of $f$ is shown below.\\\\*\n',
  'The vertex is at $P(2,1)$ and the $y$-intercept is at $Q(0, 3)$.\\\\*\n',
  '\n',
  '\\begin{figure}[!htbp]\n',
  '\\begin{center}\n',
  '\\begin{tikzpicture}\n',
  '\n',
  '    %grid\n',
  '    %\\draw [thin, color=lightgray,, xstep=1.0cm,ystep=1.0cm] (-5.5,-5.5) grid (5.5,5.5);\n',
  '    %\\draw [thin, color=lightgray,, xstep=0.2cm,ystep=0.2cm] (-5.5,-1.5) grid (5.5,16.5);\n',
  '\n',
  '    \\foreach \\x in {-2, -1,1,2,3,4,5,6}\n',
  '    \\draw[shift={(\\x,0)},color=black] (0pt,-3pt) -- (0pt,3pt) node[below]  {$\\x$};\n',
  '\n',
  '    \\foreach \\y in {-1,1,2,3,4,5,6}\n',
  '    \\draw[shift={(0,\\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left]  {$\\y$};\n',
  '\n',
  '    \\draw [thick, ->] (-2.5,0) -- (+6.5,0) node [right] {$x$};\n',
  '    \\draw [thick, ->] (0,-1.5) -- (0,6.5) node [left] {$y$};\n',
  '\n',
  '    \\draw (2,1) circle[radius=2pt] node [below] {$P$};\n',
  '    \\fill (2,1) circle[radius=2pt];\n',
  '    \\draw (0,3) circle[radius=2pt] node [right] {$Q$};\n',
  '    \\fill (0,3) circle[radius=2pt];\n',
  '\n',
  '    \\draw [<->] plot[domain= -1:5] (\\x, .5*\\x*\\x -2*\\x +3);\n',
  '\n',
  '\\end{tikzpicture}\n',
  '\\end{center}\n',
  '\\end{figure}\n',
  '\n',
  '\\begin{enumerate}\n',
  '    \\item Write down the equation of the axis of symmetry.\n',
  '    \\item The function $f$ can be written in the form $f(x)=a(x-h)^2 +k$. \\\\*\n',
  '    Write down the value of $h$ and of $k$.\n',
  '    \\item Find $a$.\n',
  '\\end{enumerate}\n'],
 'logs': ['\\item $\\log_5 25$\n',
  '\\item $\\log_6 4 + \\log_6 9$\n',
  '\\item $\\log 200 - \\log 2$\n'],
 'substitution': ['\\item Given $f(x) = x^2+3$ find $f(3)$\n',
  '\\item Given $f(x) = \\sqrt[3]{8 x^{2}}$ find $f(8)$\n',
  '\\item $\\displaystyle \\left( x y^{\\frac{1}{4}}\\right)^2$\n',
  '\\item Given $f(x) = \\log_5 x$ find $f(125)$\n',
  '\\item Given $f(x)=(x^2+3x+9)$ find $f(x-2)$\n'],
 'g-quad-vertex': ['\\item Given $f(x) = x^2+3$ find $f(3)$\n',
  '\\item Given $f(x) = \\sqrt[3]{8 x^{2}}$ find $f(8)$\n',
  '\\item $\\displaystyle \\left( x y^{\\frac{1}{4}}\\right)^2$\n'],
'exponent-fin': ['\\item Given $f(x) = x^2+3$ find $f(3)$\n',
 '\\item Given $f(x) = \\sqrt[3]{8 x^{2}}$ find $f(8)$\n',
 '\\item $\\displaystyle \\left( x y^{\\frac{1}{4}}\\right)^2$\n']}
    return bank
