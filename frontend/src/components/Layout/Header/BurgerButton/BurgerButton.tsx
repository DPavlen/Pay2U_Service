import './BurgerButton.scss';
import { MouseEventHandler, ReactElement } from 'react';

interface BurgerButtonProps {
  handleMenuOpen: MouseEventHandler<HTMLButtonElement>;
  isMenuOpen: boolean;
}

function BurgerButton({ handleMenuOpen, isMenuOpen }: BurgerButtonProps): ReactElement {

  return (
    <>
      <button onClick={handleMenuOpen} className={`burger-btn ${isMenuOpen ? 'burger-btn_active' : ''}`}>
        <span className="burger-btn__bar-top"></span>
        <span className="burger-btn__bar-mid"></span>
        <span className="burger-btn__bar-bot"></span>
      </button>
    </>
  );
}

export default BurgerButton;
