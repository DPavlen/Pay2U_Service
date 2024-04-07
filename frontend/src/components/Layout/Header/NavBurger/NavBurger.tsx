import { ReactElement } from 'react';
import './NavBurger.scss';
import { Link } from 'react-router-dom';
import homeIcon from '../../../../images/icons/home.svg';
import subscribesLogo from '../../../../images/icons/subscribes.svg';
import walletIcon from '../../../../images/icons/wallet.svg';
import calendarIcon from '../../../../images/icons/calendar.svg';
import faqIcon from '../../../../images/icons/faq.svg';
import Overlay from '../../../Overlay/Overlay.tsx';

interface NavBurgerProps {
  handleMenuOpen: () => void,
  handleMenuClose: () => void,
  isMenuOpen: boolean;
}

function NavBurger(props: NavBurgerProps): ReactElement {
  return (
    <>
      <nav className={ `nav-burger nav-burger_${ props.isMenuOpen ? 'active' : '' }` }>
        <ul>
          <li>
            <Link onClick={props.handleMenuClose} className="link" to="/"><img src={ homeIcon } alt=""/>Главная</Link>
          </li>
          <li>
            <Link onClick={props.handleMenuClose} className="link" to="/user/my-subscriptions"><img src={ subscribesLogo } alt=""/>Мои подписки</Link>
          </li>
          <li>
            <Link onClick={props.handleMenuClose} className="link" to="/user/my-payments"><img src={ walletIcon } alt=""/>История платежей</Link>
          </li>
          <li>
            <Link onClick={props.handleMenuClose} className="link" to="/faq"><img src={ faqIcon } alt=""/>Частые вопросы</Link>
          </li>
        </ul>
      </nav>
      <Overlay handleMenuOpen={props.handleMenuOpen} isMenuOpen={ props.isMenuOpen }/>
    </>
  );
}

export default NavBurger;
