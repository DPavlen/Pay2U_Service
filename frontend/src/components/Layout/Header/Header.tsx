import { ReactElement } from 'react';
import './Header.scss';
import BurgerButton from './BurgerButton/BurgerButton.tsx';
import NavBurger from './NavBurger/NavBurger.tsx';


interface HeaderProps {
  handleMenuOpen: () => void
  handleMenuClose: () => void,
  isMenuOpen: boolean
}

function Header(props: HeaderProps): ReactElement {

  return (
    <header className="header">
      <BurgerButton handleMenuOpen={ props.handleMenuOpen } isMenuOpen={ props.isMenuOpen }/>
      <NavBurger handleMenuClose={props.handleMenuClose} handleMenuOpen={props.handleMenuOpen} isMenuOpen={ props.isMenuOpen }/>
    </header>
  );
}

export default Header;
