import { ReactElement } from 'react';
import CardListHeader from '../CardListHeader/CardListHeader.tsx';
import CardList from '../CardList/CardList.tsx';
import { ICategory } from '../../utils/interfaces/interfaces.ts';

interface ICategoriesListProps {
  servicesCategories: ICategory[],
  link: string
}

function CategoriesList(props: ICategoriesListProps): ReactElement {
  return (
    <section>
      <CardListHeader title={ 'Каталог' } link={ props.link }/>
      <CardList items={ props.servicesCategories }/>
    </section>
  );
}

export default CategoriesList;
